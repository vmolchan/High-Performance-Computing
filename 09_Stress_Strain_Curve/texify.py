#!/usr/bin/env python

import matplotlib 
matplotlib.use("pgf") 
pgf_with_latex = {"pgf.texsystem": "pdflatex"}
matplotlib.rcParams.update(pgf_with_latex)

from assignment9 import Plotter 

p = Plotter("data.dat")
p.plot_pgf("ss_plot")

