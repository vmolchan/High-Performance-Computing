
# coding: utf-8

# # Assignment 7
# 
# This repository contains a file `data.dat` that is actual tabular data from a stress-strain test conducted in a standard test frame (MTS machine).  The columns of data have the following format
# 
# |time|Axial Displacement|Axial (engineering) Strain| Axial Force |
# |:-:|:-:|:-:|:-:|
# | (s) | (in) | (in/in) | (lbf) |
# 
# Complete the function definition below for the function named `convert_to_true_stress_and_strain()`.  This function should take the name of a file (e.g. `data.dat`) as an argument and return a 2-tuple ($\varepsilon_T$, $\sigma_T$), where $\varepsilon_T$ is the *true* strain and $\sigma_T$ is the *true* stress.
# 
# Recall that the definition of engineering stress is
# 
# $$
# \sigma_E = \frac P A_o
# $$
# 
# where $P$ is the axial force and $A_o$ is the original cross-sectional area of the sample.  The cross-sectional area can be computed from the width and thickness dimensions that are stored on the 3rd line of the header of the MTS data file.  Look for `Wo=` and `Thicko=`.

# Your function should parse these values out computationally (not manually) because we expect them to be in every MTS header the same way and woud like the function to work on multiple data files.
# 
# The conversion between engineering $\varepsilon_E$ and true strain is
# 
# $$
# \varepsilon_T = \ln(1+\varepsilon_E).
# $$
# 
# The conversion between engineering and true stress is
# 
# $$
# \sigma_T = \sigma_E (1+\varepsilon_E).
# $$
# 
# Use Numpy data structures and broadcasted operations to make your code compact and efficient.
# 
# ## Please Note
# 
# You may write your code directly in the Jupyter Notebook below or convert the notebook to a plain Python file with the command
# 
# ```bash
# jupyter nbconvert --to python assignment7.ipynb
# ```
# 
# which will create a file `assignment7.py`.  If you commit this file to the repository, only the Python file will be tested (not the Jupyter notebook).  However, if you do not commit this file into the repository, the Jupyter notebook will be converted automatically on Travis before testing.  

# In[26]:


import numpy as np  
import re
import linecache
datafile = 'data.dat'

def extract_width_thickness(filename):
    for line in open(filename):
        if "Wo=" in line:
            s = re.split("[\"\=]+",line)
    return (float(s[1]), float(s[3]))
#     line = linecache.getline(filename, 3)
#     width = float(line.split('=')[1].split('"')[0])
#     thickness = float(line.split('=')[2].split('"')[0])
#     return (width, thickness)

def convert_to_true_stress_and_strain(filename):
    
    (w, t) = extract_width_thickness(filename)
    A_0 = w*t
    
    df = np.loadtxt(datafile, skiprows = 5)
    E_e = df[:,2]
    P = df[:,3]

    sig_T = (P/A_0)*(1+E_e)
    E_T = np.log(1+E_e)
    
   
    
    
    
    return (E_T, sig_T)


# In[27]:


(sig, et) = convert_to_true_stress_and_strain(datafile)


# In[28]:


sig


# In[29]:


et


# In[23]:


(w, t) = extract_width_thickness(datafile)


# In[24]:


w


# In[25]:


t

