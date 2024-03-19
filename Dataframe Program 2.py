# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 14:54:02 2022

@author: Brine
"""

###############################################
### MElanie Navarrete                       ###
### CSC 226 Dataframe Program Two           ###
###############################################

### Importing Libraries ###

import numpy as np
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt

##Declaring Variables and Importing the File ##
##Folder and Path##
path_to_folder = 'C:/Users/Brine/OneDrive/Documents/CSC 140'
file_name = '/students.xlsx'

##Load data from file into dataframe ##
df_students = pd.read_excel(path_to_folder + file_name)

### load additional data into separate dataframe ##
path_to_folder = 'C:/Users/Brine/OneDrive/Documents/CSC 140'
file_name = '/students1.xlsx'
df_students_second = pd.read_excel(path_to_folder + file_name)

###Renaming the columns in the name/student, grade/level, average/gpa category## 
df_students_second.rename(
    columns = {
        'Name' : 'Student',
        'Grade' : 'Level',
        'Average' : 'GPA'
    }
    , inplace = True
)

##Merging the dat##aframes
df_students = pd.merge (
    left = df_students,
    right = df_students_second,
    on = 'Student'
)


##Display the dataframe
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.colheader_justify', 'center')
pd.set_option('display.precision', 3)

display(df_students)

##Removing Extra Fields and fixing new name errors##
df_students.drop(["Age_y", "Level_y", "GPA_y", "School_y"], axis = 1, inplace = True)
df_students.rename(
    columns = {
        'Age_x' : 'Age',
        'Level_x' : 'Level',
        'GPA_x' : 'GPA',
        'School_x' : 'School'
    }
    , inplace = True
)

##Grouping and printing the average, minimum and maximum 
result = df_students.groupby('Level').agg({'GPA': ['mean', 'min', 'max']})
  
print("Mean, min, and max values of Grade point average grouped by Grade")
print(result)

# generate a pie chart based on the data
df_students(['Level']).sum().plot(kind='bar', y='GPA')
plt.show()