###############################################
### MElanie Navarrete                       ###
### CSC 226 Dataframe Practice program      ###
###############################################

### Importing Libraries ###
#pip install numpy
#pip install pandas
#pip install openpyxl
#pip install matplotlib


### import libraries ###
import pandas as pd
import numpy as np


### declaring variables and file/ folder location ###
# folder where file with data is
path_to_folder = 'C:/Users/Brine/OneDrive/Documents/CSC 140'
# name of file where data is
file_name = '/students.xlsx'


### loading data ###
# load data from file into dataframe
df_students = pd.read_excel(path_to_folder + file_name)


### printing dataframe ###
print( df_students )


### Save data to files ###
# folder where to save file with data 
path_to_folder = 'C:/Users/Brine/OneDrive/Documents/CSC 140'

# name of file where to save data 
file_name_xls = '/students_new.xlsx'
file_name_csv = '/students_new.csv'

# save data as Excel file 
df_students.to_excel(path_to_folder + file_name_xls, index=False)
# save data as CSV file 
df_students.to_csv(path_to_folder + file_name_csv, index=False)


### quick info and stats about a dataframe ###
# info about a dataframe
print( df_students.info() )

# showing the information in the frame
print( df_students.describe() )


### setting up columns data types ###
df_students = pd.read_excel(
    path_to_folder + file_name
    , header=0
    , dtype={
        'Average':np.int64
        ,'Name':str
        ,'Age':int
        ,'Grade':int
    }
)



### Reload Data ###
# reloading data to have a clean dataframe
df_students = pd.read_excel(path_to_folder + file_name)


#

# show top 2 rows
print( df_students.head(2) )


# show bottom 2 rows
print( df_students.tail(2) )




# select rows by index: slicing
print( df_students[2:4] )

# showing students whose grades are over 75
print( df_students[ df_students["Grade"] >= 75 ] )

## displaying student grade info##
print("")
print("Student Average 75 and over")



### select rows by two conditions; grades 11 and 12 
# with an average of 75 and up ###
print("")
print("Students in grade 11 and 12 with an average of 75 and up")
print( df_students[
    (
        ( df_students["Average"] >= 75 )
        &
        ( df_students["Grade"] == 11)
    )
    |
    (
         ( df_students["Average"] >= 75 )
         &
         ( df_students["Grade"] == 12)    
    )
] )


### Adding to the dataframe ###

## Adding colums ##

# add one column with a constant column
df_students["School"] = "New Utrecht"
print( df_students )


# save to file, if needed
df_students.to_excel(path_to_folder + file_name_xls, index=False)


## Adding rows ##

# load additional data into separate dataframe
path_to_folder = 'C:/Users/Brine/OneDrive/Documents/CSC 140'
file_name = '/students1.xlsx'
df_students_addendum = pd.read_excel(path_to_folder + file_name)

# extending dataframe
df_students_all = df_students.append(df_students_addendum)
print( df_students_all )

# resetting index
df_students_all.reset_index(inplace=True,drop=True)
print( df_students_all )


### Groups and Aggregates ###

# define how to group data: group data by Grade
df_students_groupby_grade = df_students_all.group("Grade")

# print the groups in the group-by'd dataframe
print( df_students_groupby_grade.groups )

# print data from average
print( df_students_groupby_grade.get_groupby("Average") )

# print data from all groups
for average, group in df_students_groupby_grade:
    print(average)
    print(group)
    print()


## Calculating and Displaying the aggregates ##
 
df_students_groupby_average = df_students_all.groupby("Average")
df_students_avg_average = df_students_groupby_grade["Average"].agg(np.mean)
print( df_students_avg_average )


### Charting ###

#* import last library -matlab**
import matplotlib.pyplot as plt

# define how to group data
df_games_groupby_grade = df_students_all.groupby("Grade")

# calculate the aggregate: average per grade
df_students_avg_grade = df_students_groupby_average["Average"].agg(np.mean)

# generate a pie chart based on the data
df_students_avg_grade.plot(kind="pie")

plt.show()


