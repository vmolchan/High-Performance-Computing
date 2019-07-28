# Assignment 2

The aim of this assignment is to continue familiarization with git and basic Unix commands.

## Instructions

 1. In the repository, we have the directory `files1` with a file `lorem1.txt` inside it. Create a copy of `lorem1.txt` called `lorem2.txt` inside the `files1` directory.

 2. Use `cat` to concatenate `lorem1.txt` and the newly created `lorem2.txt`, redirecting the output to a new file `lorem3.txt` inside the `files1` directory.

 3. Recursively copy `files1` to `files2`.

    Your final directory/file structure for the repository should appear as

    ```
    assignment2/
    ├── .travis.yml
    ├── README.md
    ├── test.py
    ├── files1/
    |   ├── lorem1.txt
    |   ├── lorem2.txt
    |   └── lorem3.txt
    └── files2/
        ├── lorem1.txt
        ├── lorem2.txt
        └── lorem3.txt
    ```

 4. Add the newly created files/directories to your `git` repository, commit, and push the changes to Github for submission.

 ## Testing

 If you would like to check to see if your solution is correct, simply run the following command at the Terminal command prompt.

```
>python test.py
```
