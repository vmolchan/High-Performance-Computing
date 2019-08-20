# Homework Assignment 13


In [Assignment 12](https://github.com/PGE383-HPC-Fall2018/assignment12) we used [SWIG](www.swig.org) to generate Python "wrappers" to some C code to be called from a Python script that solves the Laplace equation in two dimensions.  If you recall, there were several manual steps which included calls to SWIG and a complicated compiler command to generate the compiled library.  Your task in this assignment is to use CMake to automate these steps.  Look at the file `CMakeLists.txt` in the `src` directory.  There are some comments that indicate where you should add CMake commands.

**Tips**:

 1. You will need to build a static library from the source file `iterate.c`.  

 2. You will need to generate a SWIG Python interface from the `iterate.i` file.  Look at the [`swig_add_library()`](https://cmake.org/cmake/help/v3.8/module/UseSWIG.html) command.  You will then need to link the SWIG module to the library you created from `iterate.c`


## Testing

If you would like to check to see if your solution is correct, run the following commands in sequence at the Terminal command line:

```bash
>mkdir build
>cd build
>cmake ..
>make
>ctest
```
