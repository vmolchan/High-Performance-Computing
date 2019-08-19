#!/usr/bin/env python

from mpi4py import MPI
import assignment9
import glob
comm = MPI.COMM_WORLD

filenamesfordata = glob.glob('*.dat')
file1 = 'data_%u.dat'%comm.rank
file2 = 'plot_%u'%comm.rank



P = assignment9.Plotter(filenamesfordata[comm.rank])
P.plot_png(file2)

