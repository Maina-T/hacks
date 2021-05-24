#### To remove a file from the Git repository and from the local filesystem ####
    # $ git rm file1.txt
    # $ git commit -m "remove file1.txt" # commit your changes
    # $ git push -u origin branch_name  # push your changes

#### Remove the file only from the Git repository and not remove it from the local filesystem ####
    # $ git rm --cached file1.txt
    # $ git commit -m "remove file1.txt" # commit your changes
    # $ git push -u origin branch_name  # push your changes

#### To remove directory from the Git respository and from the filesystem ####
    # $ git rm -r directory
    # $ git commit -m "remove directory" # commit your changes
    # $ git push -u origin branch_name  # push your changes
