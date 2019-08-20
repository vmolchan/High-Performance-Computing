# Homework Assignment 20

In this assignment the objective is to solve the a nonlinear equation using  NOX, i.e.

![equation](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%5E2%20u%28x%29%7D%7B%5Cpartial%20x%5E2%7D-k%20u%28x%29%5E2%20%3D%200)

with constant Dirchelet boundary conditions.  ![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20k) is a constant parameter that controls the strength of the  nonlinearity.  Use a finite difference discretization with constant grid spacing.

Your assignment is to complete the required `computeF()` function in the class `OneDimNonlinear`.  You must perform an import operation to communicate off-processor "overlaped" nodal values withing `computeF()` and fill the argument vector `F` with the residual from the finite difference operation.

Your code should be parallel consistent, i.e. it should produce the exact same answer independent of the number of processors you specify.

## Testing

If you would like to check to see if your solution is correct, run the following commands at the Terminal command line:

```bash
mpiexec -np 1 python test.py
mpiexec -np 2 python test.py
mpiexec -np 3 python test.py
```
