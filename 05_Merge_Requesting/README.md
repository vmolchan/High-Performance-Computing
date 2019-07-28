# Assignment 5

## Instructions

1. The repository contains a file `hello.c` which is a "Hello, World!" program written in the `C` programming language.  However, the file has a few syntax mistakes that is preventing it from compiling.  The correct code/syntax should be

   ````C
   #include <stdio.h>
   int main()
   {
      printf("Hello, World!");
      return 0;
   }
   ````

   Create a new branch of the repository called `bugfix` and make the necessary edits to the file to get it to compile correctly in this branch.

2. Commit changes to the `bugfix` branch and push those changes back to Github (do not merge with `master` locally).

3. In Github, create a pull request to merge the `bugfix` branch into `master`.  I will act as a collaborator and merge your pull requests.  If the tests do not pass on master, I will use the Github interface to request additional changes to the code.

## Testing

If you would like to check to see if your edits to `hello.c` are correct simply run 

````bash
gcc hello.c
./a.out > hello.txt
````
 
followed by the command `python test.py` at the command prompt.  A status message of `OK` indicates you have the correct answer. 
