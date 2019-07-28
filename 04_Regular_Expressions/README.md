# Assignment 4


## Instructions

 1. The repository contains a file `sifs.txt` with the following text:

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
    
    Using only `grep`, and pipes (`|`) along with regular expressions, write a **single line** command (it's okay to pipe the output of one `grep` command into another) that will extract **only** the numerical values after the text `sifs for crack #` from the file. The output after running your command should be:

        1.473248 2.027327
        2.043960 2.043960
        2.027327 1.473248

 1. After you have verified your command works by printing the results to `stdout` wrap the entire command in quotes and use the quoted command as an argument to `echo` followed by a redirect `>` to a file called `parse1.sh`.

    - **Example**: If your final command is `grep -i blah`, then you should run:

        ```bash
        echo 'grep -i blah' > parse1.sh
        ```
 1. Repeat 1-2, this time writing a command that will extract the same numerical values, while **omitting** the value for `sif for crack 2`.  Redirect the command to an executable script named `parse2.sh`

 1. Add `parse1.sh` and `parse2.sh` to the git repository, commit, and push back to Github.

 ## Testing

 If you would like to check to see if your solution is correct, simply run 

 ```
 bash parse1.sh > grep1.out
 ```
 
 and 

 ```
 bash parse2.sh > grep2.out
 ```
 
 followed by the command `python test.py` at the command prompt.  A status message of `OK` indicates you have the correct answer. 
