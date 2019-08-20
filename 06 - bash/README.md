# Assignment 6

## Instructions

1. Clone the repository with the following command 

   ```bash
   git clone https://github.com/PGE383-HPC-Fall2018/pge383_assignment6-[your_github_username].git $HOME/.dotfiles
   ```

   Where `[your_github_username]` is replaced with your actual Github username.  This will clone the repository into a hidden directory in `$HOME`.

2. There is a template `bash_profile` in the repository.  **Move** the existing `.bashrc` file into the repository and name it `bashrc`.

4. Add logic to the `bash_profile` that checks to see if the file `$HOME/.bashrc` exists, if and only if it does exist, then `source` it from the `bash_profile ` file.

5. Add "vi mode" command line editing to your `bash_profile`.

6. Add the following alias *exactly as is appears* to the **first line** of `bashrc`:

   ```bash
   alias lla='ls -la'
   ```

## Testing

If you would like to check to see if your edits to `bash_profile` and `bashrc` are correct simply run 

````bash
ln -s $HOME/.dotfiles/bashrc $HOME/.bashrc
source bash_profile
alias lla > lla.txt
````
 
followed by the command `python test.py` at the command prompt.  A status message of `OK` indicates you have the correct answer. 

## Not required but possibly useful

You can keep the files `bashrc` and `bash_profile` in this repository and add to them over time, storing you own customizations. To have them automatically loaded at every login, run the following commands once:

```bash
ln -s $HOME/.dotfiles/bashrc $HOME/.bashrc
rm $HOME/.bash_profile
ln -s $HOME/.dotfiles/bash_profile $HOME/.bash_profile
```
