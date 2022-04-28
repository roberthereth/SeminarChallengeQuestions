# MCM Data Prep Python Application


## Description

This application was made for the CS-495 class at Carroll College. The purpose of this app is to read a CSV file with Math Modeling Competition results. 
The program is a simple Python file, and Python must be installed in order to use this application. 
The data will be given in two CSV files once done running: "Institutions.csv" and "Teams.csv". These files also have a shared column titled "Institution ID" 
so that they may be linked within a SQL database. 



## Made by

Robert Hereth



## Before Using

In order to ensure that no data is lost, each entry in the "Institutions.csv" file assumes uniqueness. 
If there is a misspelling, difference in capitalization, or data inconsistencies within the same institution, they are counted seperately for the purpose of 
this application (ie. Missing/different data results in duplicate entries.). 
To minimize this, be sure to check the dataset before feeding it in to the application.


## How to Use

First off, make sure this application is placed in a folder of its own. Once the application is done running, the required CSV files will be in that folder.


The following packages need to be installed in order to properly run the application:

- `pandas`
- `tkinter`


Once these packages are installed, run the 'mcmDataPrep.py' file however you want. You will be prompted with a file explorer window. Select the CSV 
containing the MCM data you want to split, and hit 'Open'. Within seconds, your new split CSV files will be within the program folder. Running the program again 
will result in an override of the CSV files if not moved before running.
