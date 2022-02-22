import csv
import matplotlib.pyplot as plt
import numpy as numpy

# Gathers user data from csv file
#  scrapes: id, sex, height, weight, year started
file = open('user.csv', encoding="utf8")
csvreader = csv.reader(file)

header = []
header = next(csvreader)
header = [header[0], header[5], header[6], header[7], header[8]]
# print("scraped from user.csv: ", header)

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
# print("scraped from ascent*.csv: ", header1)

rows1 = []
for row1 in csvreader1:
    rows1.append(row1)

ascent_data = []
for row1 in rows1:
    ascent_row = [row1[1], row1[2]]
    ascent_data.append(ascent_row)
file1.close()


########## BMI vs relative grade sent scatter plot ##########

# find BMI of each user --  weight/height^2
user_bmi = {}  #Dictionary of [user_id]:[bmi]
for user in user_data:
    weight = float(user[3])
    height = float(user[2])
    if user[0] in user_bmi.keys(): # if user exists, just append BMI
        if height != 0 and weight != 0:
            calc_bmi = weight/((height/100)**2)
            round(calc_bmi, 3)
            user_bmi[user[0]].append(calc_bmi)
    else:
        if height != 0 and weight != 0:
            calc_bmi = weight/((height/100)**2)
            round(calc_bmi, 3)
            user_bmi[user[0]] = calc_bmi

x_points = [] #Grade of climb sent
y_points = [] #BMI of climber

for climber in ascent_data:
    if climber[1].isnumeric():
        x_points.append(int(climber[1]))
        y_points.append(user_bmi.get(climber[0]))

# limit bmi points to a reasonable bmi range of 12-40 (due to user input errors)
index = 0
while index < len(x_points):
    if y_points[index] is None or y_points[index]<12 or y_points[index]>40:
        del x_points[index]
        del y_points[index]
    else: 
        index = index+1

# create and maintain order for graphin purposes
x_points_conv = ["VB", "V0", "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", 
          "V10", "V11", "V12", "V13", "V14", "V15"]
y_points_conv = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
# convert difficulty ratings to V-Scale
for i in range(len(x_points)):
    ### grade_id 0-16   VB
    if x_points[i]<=16:
        x_points_conv.append("VB")
        y_points_conv.append(y_points[i])
    ### grade_id 17-28  V0
    elif x_points[i]>=17 and x_points[i]<=28:
        x_points_conv.append("V0")
        y_points_conv.append(y_points[i])
    ### grade_id 29-32  V1
    elif x_points[i]>=29 and x_points[i]<=32:
        x_points_conv.append("V1")
        y_points_conv.append(y_points[i])    
    ### grade_id 33-35  V2
    elif x_points[i]>=33 and x_points[i]<=35:
        x_points_conv.append("V2")
        y_points_conv.append(y_points[i])
    ### grade_id 36-38  V3
    elif x_points[i]>=36 and x_points[i]<=38:
        x_points_conv.append("V3")
        y_points_conv.append(y_points[i])
    ### grade_id 39-42  V4
    elif x_points[i]>=39 and x_points[i]<=42:
        x_points_conv.append("V4")
        y_points_conv.append(y_points[i])
    ### grade_id 43-46  V5
    elif x_points[i]>=43 and x_points[i]<=46:
        x_points_conv.append("V5")
        y_points_conv.append(y_points[i])    
    ### grade_id 47-50  V6
    elif x_points[i]>=47 and x_points[i]<=50:
        x_points_conv.append("V6")
        y_points_conv.append(y_points[i])
    ### grade_id 51-52  V7
    elif x_points[i]>=51 and x_points[i]<=52:
        x_points_conv.append("V7")
        y_points_conv.append(y_points[i])
    ### grade_id 53-55  V8
    elif x_points[i]>=53 and x_points[i]<=55:
        x_points_conv.append("V8")
        y_points_conv.append(y_points[i])
    ### grade_id 56-58  V9
    elif x_points[i]>=56 and x_points[i]<=58:
        x_points_conv.append("V9")
        y_points_conv.append(y_points[i])
    ### grade_id 59-60  V10
    elif x_points[i]>=59 and x_points[i]<=60:
        x_points_conv.append("V10")
        y_points_conv.append(y_points[i])
    ### grade_id 61-63  V11
    elif x_points[i]>=61 and x_points[i]<=63:
        x_points_conv.append("V11")
        y_points_conv.append(y_points[i])
    ### grade_id 64-65  V12
    elif x_points[i]>=64 and x_points[i]<=65:
        x_points_conv.append("V12")
        y_points_conv.append(y_points[i])
    ### grade_id 66-67  V13
    elif x_points[i]>=66 and x_points[i]<=67:
        x_points_conv.append("V13")
        y_points_conv.append(y_points[i])
    ### grade_id 68-69  V14
    elif x_points[i]>=68 and x_points[i]<=69:
        x_points_conv.append("V14")
        y_points_conv.append(y_points[i])
    ### grade_id 70+    V15   
    elif x_points[i]>=70:
        x_points_conv.append("V15")
        y_points_conv.append(y_points[i])


# find average BMI of all climbers
mean_bmi = float(0)
count = 0
for bmi in y_points:
        mean_bmi = mean_bmi + bmi
        count = count+1
mean_bmi = mean_bmi/count
print("Average BMI of ", count, " climbers: ", "%.3f" % mean_bmi)


# Scatter plot
plt.scatter(x_points_conv, y_points_conv, s=20, alpha= .005)
plt.ylabel('Body Mass Index')
plt.xlabel('Climb Difficulty')
plt.ylim([10, 40])
plt.show()

