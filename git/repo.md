# Git & Github Repository Demo
*Create a free github account*: [GitHub](https://github.com)

## Create New Repo
  - Give repo a name:  **project_name**
  - Description (optional): *Brief description of project*
  - Set privacy: **Public | Private**
  - Click green button: **Create repository**

## Git Commands
  - __git clone:__ is a git command, which creates a clone/    copy of an existing repository into a new directory.

    Example:
    ```
    #git clone <url>:
    $ git clone http://example.com/gitproject.git
    ```
  
    - Change to newly create repo directory

    Example:
    ```
    cd project_name
    ```

    - Create a new file in directory

    Example:
    ```
    #touch <filename>
    $ touch index.html | styles.css | script.js
    ```

  - __git status:__ is a command is used to show the status of the git repository. This command displays the state of the local directory and the staging area

      Example:
      ```
      $ git status
      On branch main

      No commits yet

      Untracked files:
        (use "git add <file>..." to include in what will be committed)
              index.html

      nothing added to commit but untracked files present (use "git add" to track)

      #After git add index.html
      No commits yet

      Changes to be committed:
        (use "git rm --cached <file>..." to unstage)
              new file:   index.html
      ```

  - __git add:__ is a command, which adds changes in the working directory to the staging area. With the help of this command, you tell Git that you want to add updates to a certain file in the next commit

    Example:
    ```
    Add individual file:

    git add <filename>

    git add index.html

    Adds all files in staging area:
    
    git add .
    ```

  - __git commit:__ is the term used for saving changes. Git does not add changes to a commit automatically. You need to indicate which file and changes need to be saved before running the Git commit command. The commit command does not save changes in remote servers, only in the local repository of Git

      Example:
      ```
      # Commits all the changed files with "Commit Message"
      $ git commit -m "Commit Message"

      # Adds/Removes and Commits in a single command
      $ git commit -a
      
      # Adds/Removes and Commits in a single command with "Commit Message"
      $ git commit -am "Commit Message"
      ```

  - __git push:__ push command allows you to send (or push) the commits from your local branch in your local Git repository to the remote repository

      Example:
      ```
      $ git push
      Enumerating objects: 1, done.
      Counting objects: 100% (1/1), done.
      Delta compression using up to 2 threads
      Compressing objects: 100% (1/1), done.
      Writing objects: 100% (1/1), 195.90 KiB | 1.48 MiB/s, done.
      Total 1 (delta 1), reused 0 (delta 0), pack-reused 0      
      remote: Resolving deltas: 100% (1/1), done.
      To http://example.com/gitproject.git
      * [new branch]      main -> main
      ```

  - __git pull:__ command first runs git fetch which downloads content from the specified remote repository. Then a git merge is executed to merge the remote content refs and heads into a new local merge commit

    Example:
    ```
    $ git pull
    Already up to date.
    ```

## Handling Merge Conflicts