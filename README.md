# itu-cli

A simple command-line tool for ITU related tasks. Implemented in python using the `argparse`, `os`, and `json` modules.

## Commands

`itu init`: Creates a JSON file to store the user's data.

`itu canteen`: Opens the website of the university's [school canteen](https://itustudent.itu.dk/Campus-Life/Student-Life/Canteen-Menu).

`itu learnit courseName`:
Opens the [LearnIT](https://learnit.itu.dk/) page of the given subject. First you have to select and add your courses by using the `-a` flag, after which you have to specify the course's 7-digit code from LearnIT. This is then stored in the JSON file alongside the coursename. You can delete a course from the JSON file using the `-d` flag.

`itu git`: Opens your GitHub account. First, you have to specify your username using the `-a` flag, which then saved into the JSON config file.

## Usage
If you want to be able to run the tool from the command line without having to use `python`, you can create a .bat file with the following contents:

    @echo off
    python path_for_the_-py_file\itu.py" %*

Add the location of this folder to your PATH variable, and after that you can use the scripts just by using `itu commandName --flagName argumentName` in the terminal.