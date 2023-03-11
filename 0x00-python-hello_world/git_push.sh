#!/bin/bash

# Prompt the user for a commit message
read -p "Enter commit message: " message

# Add all changes to the git staging area
git add .

#Commit changes with the specified message
git commit -m "$message"

# Push changes to the remote repository
git push
