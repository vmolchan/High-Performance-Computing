# High-Performance-Computing

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

 ## 07 - Stress and strain

 
