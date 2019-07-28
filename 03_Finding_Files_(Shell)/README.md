# Assignment 3


## Instructions

 1. In the repository, you will find a directories `files1` and `files2` with a set of subdirectories and files inside them. Use the Unix `find` command to locate the following files when run from the repository's root directory (this is not the files system root `/`)

    ````
    ./files1/lorem2.dat
    ./files1/lorem3.dat
    ./files2/lorem2.dat
    ./files2/lorem3.dat
    ````
    Just for clarity, the entire repository file structure is shown below, the files you are looking for are highlighted with \*\*.

    ````
    assignment3/
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

 4. Test your `find` command interactively on the command line.  Once you've figured out the correct syntax, copy your command into a new file called `myfind.sh`, you can do this by using `echo 'find <my complicated arguments>' > myfind.sh` where `<my complicated arguments>` is replaced with the correct set of arguments.  Alternatively, you could also open a new file in the text editor and add your `find` command syntax.

 5. Add `myfind.sh` to the git repository, commit, and push back to Github.

 **Hint:** You will likely need an option to restrict the depth of the search that I did not discuss in the video (because matching file names are found in the directories `files3`, `files4`, `files5`, and `files6`).  Use the `man` page or Google to assist in finding the correct options.

 ## Testing

 If you would like to check to see if your solution is correct, simply run

 ````
 bash myfind.sh > find.out
 ````

 followed by the command `python test.py` at the command prompt.  A status message of `OK` indicates you have the correct answer.
