@echo off
setlocal

:: Prompt for commit message
set /p commit_message=Please enter your commit message: 

:: Stage all changes
git add .

:: Commit with the provided message
git commit -m "%commit_message%"

:: Push to the selected branch
git push -u origin main

endlocal