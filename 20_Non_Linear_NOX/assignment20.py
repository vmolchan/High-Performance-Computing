#!/usr/bin/env python
import numpy as np

from PyTrilinos import Teuchos
from PyTrilinos import Epetra
from PyTrilinos import EpetraExt
from PyTrilinos import NOX


class OneDimNonliear(NOX.Epetra.Interface.Required):

    def __init__(self, comm, nx=10, xmin=0.0, xmax=1.0, k=1.0):
        super().__init__()

        self.comm     = comm
        self.rank = comm.MyPID()
        self.size = comm.NumProc()

        self.xmin, self.xmax = xmin, xmax

        self.nx = nx
        self.dx = (xmax - xmin) / (nx - 1)

        self.k = k

        self.create_graph()

        standard_map = self.get_standard_map()
        self.has_boundary_condition_1 = (standard_map.MinMyGID() == standard_map.MinAllGID())
        self.has_boundary_condition_2 = (standard_map.MaxMyGID() == standard_map.MaxAllGID())

        self.create_slice()

        self.boundary_condition_1 = 0.0
        self.boundary_condition_2 = 1.0

        self.create_vectors_and_importer()
        
        # non-linear has residual F(x)
        # A(x)x-b=F(x)
        # run optimizaiton routine to drive F(x) to zero
        # dR/dx delta_x = 0

    def set_boundary_condition(self, side="left", value=0.0):
        if side == "left":
            self.boundary_condition_1 = value
        if side == "right":
            self.boundary_condition_2 = value

        self.create_vectors_and_importer()


    def create_slice(self):

        standard_map = self.get_standard_map()

        if self.has_boundary_condition_1:
            s0 = 1
        else:
            s0 = None
        if self.has_boundary_condition_2:
            s1 = -1
        else:
            s1 = None

        self.slice = slice(s0, s1)


    def create_graph(self):

        standard_map = Epetra.Map(self.nx, 0, self.comm)
        self.graph = Epetra.CrsGraph(Epetra.Copy, standard_map, 3)
        for gid in standard_map.MyGlobalElements():
            # Boundaries: Dirichlet boundary conditions
            if gid in (0, self.nx - 1):
                self.graph.InsertGlobalIndices(gid, [gid])
            else:
                self.graph.InsertGlobalIndices(gid, [gid - 1, gid, gid + 1])
        self.graph.FillComplete()


    def create_vectors_and_importer(self):

        self.u = Epetra.Vector(self.graph.RowMap(), True)

        #Fill with initial guess (a straight line between boundary conditions)
        self.u[:] = self.boundary_condition_1 + (self.get_standard_map().MyGlobalElements() * 
                      (self.boundary_condition_2 - self.boundary_condition_1) / (self.nx - 1))

        self.u_overlap = Epetra.Vector(self.get_overlap_map())

        self.u_sorted_overlap = np.zeros_like(self.u_overlap[:], dtype=np.double)

        self.sorted_overlap_indices = np.argsort(self.get_overlap_map().MyGlobalElements())

        self.importer = Epetra.Import(self.get_overlap_map(), self.get_standard_map())


    def computeF(self, u, F, flag):
        """
        This is the function that NOX calls back to in order to compute F(u).
        Arguments u and F are provided as Epetra.Vector objects, complete with
        numpy interface.
        """
        #F is the residual
        # u is the unknown 'x'
        # for our case, dont need flag
        
        # I need to overlap nodes owned by precessors.
        # in two processor case, the first node of the next processor needs to be overlapped in processor 0. The            last of 0 needs to be in 1
        
        try:
            importer = self.get_importer()
            u_overlap = self.get_overlap_solution()
            u_sorted_overlap = self.get_sorted_overlap_solution()
            
            
            
            u_overlap.Import(u, importer, Epetra.Insert)
            
            u_sorted_overlap[:] = u_overlap[self.get_sorted_overlap_indices()]
            
            # want to use numpy broadcast operartions
            # needs to know boundaries
            # F[1:], F[:-1], F[:], thats what slice does
            F[self.get_slice()] = (u_sorted_overlap[:-2] - 2 * u_sorted_overlap[1:-1] +u_sorted_overlap[2:])/(self.dx * self.dx) - self.k * u_sorted_overlap[1:-1] * u_sorted_overlap[1:-1]
            
            if self.has_boundary_condition_1:
                F[0] = u_sorted_overlap[0] - self.boundary_condition_1
            if self.has_boundary_condition_2:
                F[-1] = u_sorted_overlap[-1] - self.boundary_condition_2
             
            self.u[:] = u[:]
            
            return True
            
            
        except Exception as e:
            print("Processor", self.rank,
                  "OneDimNonliear.computeF() has thrown an exception:")
            print(str(type(e))[18:-2] + ":", e)
            return False


    def solve(self):

        #Suppress 'Aztec status AZ_loss: loss of precision' messages
        self.comm.SetTracebackMode(0)

        #Get the initial solution vector
        initial_guess    = self.get_solution()
        nox_initial_guess = NOX.Epetra.Vector(initial_guess, NOX.Epetra.Vector.CreateView)

        # Define the ParameterLists
        nonlinear_parameters = NOX.Epetra.defaultNonlinearParameters(self.comm, 2)
        print_parameters = nonlinear_parameters["Printing"]
        linear_solver_parameters = nonlinear_parameters["Linear Solver"]

        # Define the Jacobian interface/operator
        matrix_free_operator = NOX.Epetra.MatrixFree(print_parameters, self, nox_initial_guess)
        # Define the Preconditioner interface/operator
        preconditioner = NOX.Epetra.FiniteDifferenceColoring(print_parameters, self, initial_guess, self.get_graph(), True)

        #Create and execute the solver
        solver = NOX.Epetra.defaultSolver(initial_guess, self, matrix_free_operator, matrix_free_operator, 
                preconditioner, preconditioner, nonlinear_parameters)

        solve_status = solver.solve()

        if solve_status != NOX.StatusTest.Converged:
            if self.rank == 0: 
                print("Nonlinear solver failed to converge")



    def get_graph(self):
        return self.graph

    def get_standard_map(self):
        return self.get_graph().RowMap()

    def get_overlap_map(self):
        return self.get_graph().ColMap()

    def get_slice(self):
        return self.slice

    def get_solution(self):
        return self.u

    def get_overlap_solution(self):
        return self.u_overlap

    def get_sorted_overlap_solution(self):
        return self.u_sorted_overlap

    def get_importer(self):
        return self.importer

    def get_sorted_overlap_indices(self):
        return self.sorted_overlap_indices

    def get_final_solution(self):

        balanced_map = self.u.Map()

        if self.rank == 0:
            my_global_elements = balanced_map.NumGlobalElements()
        else:
            my_global_elements = 0

        temp_map = Epetra.Map(-1, my_global_elements, 0, self.comm)
        solution = Epetra.Vector(temp_map)

        importer = Epetra.Import(temp_map, balanced_map)

        solution.Import(self.u, importer, Epetra.Insert)

        return solution.ExtractCopy()


if __name__ == '__main__':

    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    

    comm    = Epetra.PyComm()

    solver = OneDimNonliear(comm, nx=10, k=10)

    solver.solve()

    sol = solver.get_final_solution()

    print(sol)

    if comm.MyPID() == 0:
        x = np.linspace(solver.xmin, solver.xmax, num=solver.nx)
        plt.plot(x, sol[:])
        plt.savefig('test.png')
