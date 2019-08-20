# High-Performance-Computing Summary

### **Note:**
1. Folders 01-04 are for getting used to some simple UNIX commands.
2. Folder 05 is a simple C program.
3. Folder 06 is configuring `.bashrc` and `bash_profile`

**4. 07-21 are _Python_ projects**

## 01 - Getting Used to GitHub

### solution.txt

This assignment is just for creating a simple **.txt** file using some simple UNIX commands like `ls`, `cd`, `touch` and `vi`.

We also got familiar with some git commands including `status`, `add`, `commit`, and  `push`

## 02 - Directory Manipulation

This assignment furthers explores UNIX commands. Here we concatenate files with `cat`. Directories are created with `mkdir` and renamed/copied with `mv` and `cp`.

## 03 - Shell Script for Locating Files

### myfind.sh

Our first shell script to locate files from the repositories' root directory. The file structure is structured as follows:

````
03_Finding_Files_(Shell)/
├── .travis.yml
├── README.md
├── test.py
├── files1/
|   ├── lorem1.txt
|   ├── lorem2.txt
|   ├── lorem3.txt
|   ├── lorem1.dat
|   ├── **lorem2.dat**
|   ├── **lorem3.dat**
|   ├── files3/
|   |   ├── lorem1.txt
|   |   ├── lorem2.txt
|   |   ├── lorem3.txt
|   |   ├── lorem1.dat
|   |   ├── lorem2.dat
|   |   └── lorem3.dat
|   └── files4/
|       ├── lorem1.txt
|       ├── lorem2.txt
|       ├── lorem3.txt
|       ├── lorem1.dat
|       ├── lorem2.dat
|       └── lorem3.dat
└── files2/
    ├── lorem1.txt
    ├── lorem2.txt
    ├── lorem3.txt
    ├── lorem1.dat
    ├── **lorem2.dat**
    ├── **lorem3.dat**
    ├── files5/
    |   ├── lorem1.txt
    |   ├── lorem2.txt
    |   ├── lorem3.txt
    |   ├── lorem1.dat
    |   ├── lorem2.dat
    |   └── lorem3.dat
    └── files6/
        ├── lorem1.txt
        ├── lorem2.txt
        ├── lorem3.txt
        ├── lorem1.dat
        ├── lorem2.dat
        └── lorem3.dat
````

The UNIX command `find` was echoed with `echo` into a shell script **_myfind.sh_**. The output of this command was then put into the file **_find.out_**.


## 04 - Regular expressions

The file **sifs.txt** contains some values we want to extract.

`````
        Determining Transmissivity Coefficients  
        Average Tractions
          crack 1 traction 1.319254
          crack 2 traction 1.496583
          crack 3 traction 1.319254
        sifs for crack 1
          1.473248 2.027327
        sifs for crack 2
          2.043960 2.043960
        sifs for crack 3
          2.027327 1.473248
`````

The file contains the lines _sifs for crack {number}_ before each set of values. We use a one line `grep` command to grab these values as:

`````
        1.473248 2.027327
        2.043960 2.043960
        2.027327 1.473248
`````


 I then `echo` the command into **parse.sh**.

 ## 05 - Merge Requesting

 Here a simple **hello.c** file is created. The purpose of this assignment is to get familiar with branches in git.

 ## 06 - bash

 Setting up configurations for `.bashrc` and `bash_profile`

 ## 07 - Stress and Strain

 This project utilizes **regular expressions** to extract width and thickness for calculating engineering stress and strain.

## 08 - Simpsons & Trapezoid

In `07` we explored using regular expressions to extract information from a data file. Now, we use those values in calculating [engineering toughness](https://en.wikipedia.org/wiki/Toughness).

To calculate the integral, we use two numerical approximations:
1. [Simpsons Rule](https://en.wikipedia.org/wiki/Simpson's_rule)
2. [Trapezoidal Rule](https://en.wikipedia.org/wiki/Trapezoidal_rule)

## 09 - Stress Strain Curve Plot

The `Toughness()` class is further built upon by creating a `Plotter()` class inheriting from Toughness. A Plot method is included in here to create the Stress-Strain curve. The area under the curve is also displayed (as engineering toughness).

## 10 - Solving 2D Laplace with Numba

The **2D Laplace** equation shows up in many places in Engineering and Physics - particularly for heat conduction and pressure diffusion.

A `numba_solve()` method is added to the `LaplaceSolver` class (inheriting from `Grid`) in `laplace.py` to speed up the calculation of the 2D Laplace with given boundary conditions. The `numba_solve` method calls the `iterate` method which is a _slow_ implementation of a finite difference method using for loops. the `@jit` decorator.

**Note:** we should not expect `jit` to be faster than `numpy` vectorization.

## 11 - Solving 2D Laplace with cffi

**Note:** here we are solving the same problem as in **assignment 10**.
[cffi](https://cffi.readthedocs.io/en/latest/) is a C Foreign Function interface for Python.

A `cffi.FFI()` instance is created.

 We are able to use existing C Libraries with `dlopen()`. We can then use the `cdef` method to pass in our C function header.

 We further develop our `LaplaceSolver` class in `laplace.py` to implement an [API or ABI](https://cffi.readthedocs.io/en/latest/overview.html#abi-versus-api) version of the Laplace Solver with `cffi_solve_abi` and `cffi_solve_api`.

## 12 - Solving 2D Laplace with SWIG

Similar to the last two assignments, we are still solving the 2D Laplace. This time we use [SWIG](http://www.swig.org).

`SWIG` is useful for wrapping C and C++ library functions, particularly when the function headers are identical.

We have two functions `iterate` and `iterate_red_black` which are written in C. A SWIG interface file `iterate.i` is written that wraps the two functions. The function declarations are in the `iterate.h` header file. We then create `swig_solve` and `swig_solve_red_black` methods in `LaplaceSolver` in `laplace.py`.

## 13 - cmake

Here we use CMake to automate calls to SWIG (like in assignment 12) and compiler commands.

## 14 - Parallel Reading of Files

For two indepentent data files, reading them in can be though of as an [_embarrassingly parallel_](https://en.wikipedia.org/wiki/Embarrassingly_parallel) process. We can break up the task of processing files to multiple processors. We utilize [mpi4py](https://mpi4py.readthedocs.io/en/stable/) to read in two data files in parallel. These files are then passed into the `Plotter` instance (from **09**) and the Stress Strain curve is calculated.

## 15 - Parallel Integration of Stress Strain

Now that we have explored reading files in parallel, we can break up the task of integreation to multiple processors. Evaluation of definite integrals is also an _embarrassingly parallel_ process.

In `assignment15.py` we build out the `ParallelToughness` class which inherits from `StressStrainConverter` in **08** utilizing `mpi4py`. The process will follow a primary/secondary model (commonly referred to as master/slave). One processor will serve as the `primary` splitting data amongst the other `secondary` processors. This can be seen in the `init` method.

The class methods will be executed in parallel to calculate engineering toughness.

## 16 - Parallel Gauss Quadrature

**Gauss Quadrature** is a numerical [method](https://en.wikipedia.org/wiki/Gaussian_quadrature) for evaluating a definite integral. We will use `fixed_quad()` in `scipy` to evaluate an arbitrary integral.

Splitting the data evenly across processors is not the most interesting implementation of a parallel program. Instead, it would be more efficient to delegate tasks as a processor becomes available since some regions of the integral are more computationally expensive (regions with more area under the curve for a same change in x).

I have built out the `GaussTable` class, utilizing `send()`, `isend()`, `recv()`, and `gather()` from `mpi4py`. We can see that the lowest rank processor serves as the delegator, giving portions of the dataframe to other processors as they become available.
