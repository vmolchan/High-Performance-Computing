
# coding: utf-8

# # Assignment 8
# 
# This repository contains the same file `data.dat` from [Assignment 7](https://github.com/PGE383-HPC-Spring2018/assignment7) and a Python class named `StressStrainConverter` that essentially implements a solution to that assignment in an object-oriented way.
# 
# You should complete the derived class `Toughness` to compute toughness of the material from the stress strain curve.  Recall that toughness is the area under the stress-strain curve, i.e.
# 
# $$
# \mbox{Toughness} = \int \sigma \, {\rm d}\varepsilon
# $$
# 
# There are two function templates in the derived class that will be tested, `comute_toughness_simps()` which should use Simpson's rule for the integration and `compute_toughness_trapz()` which should use the trapezoid rule for the integration.  Both of these method implementations can be found in `scipy.integrate`.  Both of these functions should return the computed integral value.
# 
# If you understand and use *class inheritance* you should be able to complete this assignment with only a few lines of code.

# ## Please Note
# 
# You may write your code directly in the Jupyter Notebook below or convert the notebook to a plain Python file with the command
# 
# ```bash
# jupyter nbconvert --to python assignment8.ipynb
# ```
# 
# which will create a file `assignment8.py`.  If you commit this file to the repository, only the Python file will be tested (not the Jupyter notebook).  However, if you do not commit this file into the repository, the Jupyter notebook will be converted automatically on Travis before testing.  

# In[22]:


import numpy as np
import linecache
import scipy.integrate
import re
datafile = 'data.dat'


class StressStrainConverter():
    
    def __init__(self, filename):
        
        self.filename = filename
        

    def extract_dimensions(self):

        line = linecache.getline(self.filename, 3).split('=')

        self.width = float(line[1].split('"')[0])

        self.thickness = float(line[2].split('"')[0]) 

        return
    

    def convert_to_true_stress_and_strain(self):
        
        self.extract_dimensions()

        eng_strain, force = np.loadtxt(self.filename, skiprows=5, usecols=(2,3)).T 

        self.true_strain = np.log(1 + eng_strain)

        self.true_stress = force / self.width / self.thickness * (1 + eng_strain)

        return 
    
    
class Toughness(StressStrainConverter):
    
    
    
    def compute_toughness_simps(self):
        
        self.extract_dimensions()
        self.convert_to_true_stress_and_strain()
        
        return scipy.integrate.simps(self.true_stress, self.true_strain)
    
    def compute_toughness_trapz(self):
        self.extract_dimensions()
        self.convert_to_true_stress_and_strain()
        
        return scipy.integrate.trapz(self.true_stress, self.true_strain)

