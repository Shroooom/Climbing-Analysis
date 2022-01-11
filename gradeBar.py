import csv
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np


# Gathers user data from csv file
#  scrapes: id, sex, height, weight, year started
file = open('user.csv', encoding="utf8")
csvreader = csv.reader(file)

header = []
header = next(csvreader)
header = [header[0], header[5], header[6], header[7], header[8]]
print("scraped from user.csv: ", header)

rows = []
for row in csvreader:
    rows.append(row)

user_data = []
for row in rows:
    user_row = [row[0], row[5], row[6], row[7], row[8]]
    user_data.append(user_row)
file.close()


# Gathers Ascent data of each user from csv file
#  scrapes: user id and grade_id
##### to use a data file with more data points, comment line 30 and uncomment line 31 #####
file1 = open('ascent100k.csv', encoding="utf8")
# file1 = open('ascent750k.csv', encoding="utf8")
csvreader1 = csv.reader(file1)

header1 = []
header1 = next(csvreader1)
header1 = [header1[1], header1[2]]
print("scraped from ascent*.csv: ", header1)

rows1 = []
for row1 in csvreader1:
    rows1.append(row1)

ascent_data = []
for row1 in rows1:
    ascent_row = [row1[1], row1[2]]
    ascent_data.append(ascent_row)
file1.close()


########## grade sent vs gender bar graph ##########

x_points = ["VB ", "V0 ", "V1 ", "V2 ", "V3 ", "V4 ", "V5 ", "V6 ", "V7 ", 
            "V8 ", "V9 ", "V10", "V11", "V12", "V13", "V14", "V15"]         #grade of climb
y_pointsMale = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]      #number of male climbers who sent this grade
y_pointsFemale = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    #number of male climbers who sent this grade

user_gender = {}  #Dictionary of [user_id]:[gender]
for user in user_data:
    if user[0] in user_gender.keys():
        user_gender[user[0]].append(int(user[1]))
    else:
        user_gender[user[0]] = int(user[1])

for climber in ascent_data:
    if climber[1].isnumeric():
        if int(climber[1])<=16:                                  # grade_id 0-16   VB
            if user_gender[climber[0]] == 0:
                y_pointsMale[0] = y_pointsMale[0]+1
            else:
                y_pointsFemale[0] = y_pointsFemale[0]+1
        elif int(climber[1])>=17 and int(climber[1])<=28:  # grade_id 17-28  V0
            if user_gender[climber[0]] == 0:
                y_pointsMale[1] = y_pointsMale[1]+1
            else:
                y_pointsFemale[1] = y_pointsFemale[1]+1
        elif int(climber[1])>=29 and int(climber[1])<=32:  # grade_id 29-32  V1
            if user_gender[climber[0]] == 0:
                y_pointsMale[2] = y_pointsMale[2]+1
            else:
                y_pointsFemale[2] = y_pointsFemale[2]+1
        elif int(climber[1])>=33 and int(climber[1])<=35:  # grade_id 33-35  V2
            if user_gender[climber[0]] == 0:
                y_pointsMale[3] = y_pointsMale[3]+1
            else:
                y_pointsFemale[3] = y_pointsFemale[3]+1
        elif int(climber[1])>=36 and int(climber[1])<=38:  # grade_id 36-38  V3
            if user_gender[climber[0]] == 0:
                y_pointsMale[4] = y_pointsMale[4]+1
            else:
                y_pointsFemale[4] = y_pointsFemale[4]+1    
        elif int(climber[1])>=39 and int(climber[1])<=42:  # grade_id 39-42  V4
            if user_gender[climber[0]] == 0:
                y_pointsMale[5] = y_pointsMale[5]+1
            else:
                y_pointsFemale[5] = y_pointsFemale[5]+1
        elif int(climber[1])>=43 and int(climber[1])<=46:  # grade_id 43-46  V5
            if user_gender[climber[0]] == 0:
                y_pointsMale[6] = y_pointsMale[6]+1
            else:
                y_pointsFemale[6] = y_pointsFemale[6]+1
        elif int(climber[1])>=47 and int(climber[1])<=50:  # grade_id 47-50  V6
            if user_gender[climber[0]] == 0:
                y_pointsMale[7] = y_pointsMale[7]+1
            else:
                y_pointsFemale[7] = y_pointsFemale[7]+1
        elif int(climber[1])>=51 and int(climber[1])<=52:  # grade_id 51-52  V7
            if user_gender[climber[0]] == 0:
                y_pointsMale[8] = y_pointsMale[8]+1
            else:
                y_pointsFemale[8] = y_pointsFemale[8]+1
        elif int(climber[1])>=53 and int(climber[1])<=55:  # grade_id 53-55  V8
            if user_gender[climber[0]] == 0:
                y_pointsMale[9] = y_pointsMale[9]+1
            else:
                y_pointsFemale[9] = y_pointsFemale[9]+1
        elif int(climber[1])>=56 and int(climber[1])<=58:  # grade_id 56-58  V9
            if user_gender[climber[0]] == 0:
                y_pointsMale[10] = y_pointsMale[10]+1
            else:
                y_pointsFemale[10] = y_pointsFemale[10]+1
        elif int(climber[1])>=59 and int(climber[1])<=60:  # grade_id 59-60  V10
            if user_gender[climber[0]] == 0:
                y_pointsMale[11] = y_pointsMale[11]+1
            else:
                y_pointsFemale[11] = y_pointsFemale[11]+1
        elif int(climber[1])>=61 and int(climber[1])<=63:  # grade_id 61-63  V11
            if user_gender[climber[0]] == 0:
                y_pointsMale[12] = y_pointsMale[12]+1
            else:
                y_pointsFemale[12] = y_pointsFemale[12]+1
        elif int(climber[1])>=64 and int(climber[1])<=65:  # grade_id 64-65  V12
            if user_gender[climber[0]] == 0:
                y_pointsMale[13] = y_pointsMale[13]+1
            else:
                y_pointsFemale[13] = y_pointsFemale[13]+1
        elif int(climber[1])>=66 and int(climber[1])<=67:  # grade_id 66-67  V13
            if user_gender[climber[0]] == 0:
                y_pointsMale[14] = y_pointsMale[14]+1
            else:
                y_pointsFemale[14] = y_pointsFemale[14]+1
        elif int(climber[1])>=68 and int(climber[1])<=69:  # grade_id 68-69  V14
            if user_gender[climber[0]] == 0:
                y_pointsMale[15] = y_pointsMale[15]+1
            else:
                y_pointsFemale[15] = y_pointsFemale[15]+1
        elif int(climber[1])>=70:                                # grade_id 70+    V15   
            if user_gender[climber[0]] == 0:
                y_pointsMale[16] = y_pointsMale[16]+1
            else:
                y_pointsFemale[16] = y_pointsFemale[16]+1
        else:
            print("you should not be here")


x_axis_int = np.arange(len(x_points))
plt.bar(x_axis_int - .2, y_pointsMale, .4, label = 'Male')
plt.bar(x_axis_int + .2, y_pointsFemale, .4, label = 'Female')
plt.xticks(x_axis_int, x_points)
plt.xlabel("Grades")
plt.ylabel("Number of climbers")
plt.legend()
plt.show()