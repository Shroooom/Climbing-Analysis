import csv
import matplotlib.pyplot as plt
import numpy as numpy


# Gathers user data from csv file
#  scrapes: id, sex, hiehgt, weight, year started
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


########## BMI analysis with climbing grades sent ##########

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


# find average BMI of all climbers
mean_bmi = float(0)
count = 0
for bmi in y_points:
        mean_bmi = mean_bmi + bmi
        count = count+1
mean_bmi = mean_bmi/count
print("Average BMI of ", count, " climbers: ", mean_bmi)

# x_points -> grade_id
# y_points -> bmi of climber
# find average BMI of each grade Climber
bmi_vb = float(0)
count_vb = 0
bmi_v0 = float(0)
count_v0 = 0
bmi_v1 = float(0)
count_v1 = 0
bmi_v2 = float(0)
count_v2 = 0
bmi_v3 = float(0)
count_v3 = 0
bmi_v4 = float(0)
count_v4 = 0
bmi_v5 = float(0)
count_v5 = 0
bmi_v6 = float(0)
count_v6 = 0
bmi_v7 = float(0)
count_v7 = 0
bmi_v8 = float(0)
count_v8 = 0
bmi_v9 = float(0)
count_v9 = 0
bmi_v10 = float(0)
count_v10 = 0
bmi_v11 = float(0)
count_v11 = 0
bmi_v12 = float(0)
count_v12 = 0
bmi_v13 = float(0)
count_v13 = 0
bmi_v14 = float(0)
count_v14 = 0
bmi_v15 = float(0)
count_v15 = 0

for gradedIndex in range(len(x_points)):
    if x_points[gradedIndex]<=16:                                  # grade_id 0-16   VB
        bmi_vb = bmi_vb+y_points[gradedIndex]
        count_vb = count_vb+1
    elif x_points[gradedIndex]>=17 and x_points[gradedIndex]<=28:  # grade_id 17-28  V0
        bmi_v0 = bmi_v0+y_points[gradedIndex]
        count_v0 = count_v0+1
    elif x_points[gradedIndex]>=29 and x_points[gradedIndex]<=32:  # grade_id 29-32  V1
        bmi_v1 = bmi_v1+y_points[gradedIndex]
        count_v1 = count_v1+1
    elif x_points[gradedIndex]>=33 and x_points[gradedIndex]<=35:  # grade_id 33-35  V2
        bmi_v2 = bmi_v2+y_points[gradedIndex]
        count_v2 = count_v2+1
    elif x_points[gradedIndex]>=36 and x_points[gradedIndex]<=38:  # grade_id 36-38  V3
        bmi_v3 = bmi_v3+y_points[gradedIndex]
        count_v3 = count_v3+1    
    elif x_points[gradedIndex]>=39 and x_points[gradedIndex]<=42:  # grade_id 39-42  V4
        bmi_v4 = bmi_v4+y_points[gradedIndex]
        count_v4 = count_v4+1
    elif x_points[gradedIndex]>=43 and x_points[gradedIndex]<=46:  # grade_id 43-46  V5
        bmi_v5 = bmi_v5+y_points[gradedIndex]
        count_v5 = count_v5+1
    elif x_points[gradedIndex]>=47 and x_points[gradedIndex]<=50:  # grade_id 47-50  V6
        bmi_v6 = bmi_v6+y_points[gradedIndex]
        count_v6 = count_v6+1
    elif x_points[gradedIndex]>=51 and x_points[gradedIndex]<=52:  # grade_id 51-52  V7
        bmi_v7 = bmi_v7+y_points[gradedIndex]
        count_v7 = count_v7+1   
    elif x_points[gradedIndex]>=53 and x_points[gradedIndex]<=55:  # grade_id 53-55  V8
        bmi_v8 = bmi_v8+y_points[gradedIndex]
        count_v8 = count_v8+1
    elif x_points[gradedIndex]>=56 and x_points[gradedIndex]<=58:  # grade_id 56-58  V9
        bmi_v9 = bmi_v9+y_points[gradedIndex]
        count_v9 = count_v9+1
    elif x_points[gradedIndex]>=59 and x_points[gradedIndex]<=60:  # grade_id 59-60  V10
        bmi_v10 = bmi_v10+y_points[gradedIndex]
        count_v10 = count_v10+1
    elif x_points[gradedIndex]>=61 and x_points[gradedIndex]<=63:  # grade_id 61-63  V11
        bmi_v11 = bmi_v11+y_points[gradedIndex]
        count_v11 = count_v11+1
    elif x_points[gradedIndex]>=64 and x_points[gradedIndex]<=65:  # grade_id 64-65  V12
        bmi_v12 = bmi_v12+y_points[gradedIndex]
        count_v12 = count_v12+1
    elif x_points[gradedIndex]>=66 and x_points[gradedIndex]<=67:  # grade_id 66-67  V13
        bmi_v13 = bmi_v13+y_points[gradedIndex]
        count_v13 = count_v13+1
    elif x_points[gradedIndex]>=68 and x_points[gradedIndex]<=69:  # grade_id 68-69  V14
        bmi_v14 = bmi_v14+y_points[gradedIndex]
        count_v14 = count_v14+1
    elif x_points[gradedIndex]>=70:                                # grade_id 70+    V15   
        bmi_v15 = bmi_v15+y_points[gradedIndex]
        count_v15 = count_v15+1
    else:
        print("you should not be here")

bmi_vb = bmi_vb/count_vb
bmi_v0 = bmi_v0/count_v0
bmi_v1 = bmi_v1/count_v1
bmi_v2 = bmi_v2/count_v2
bmi_v3 = bmi_v3/count_v3
bmi_v4 = bmi_v4/count_v4
bmi_v5 = bmi_v5/count_v5
bmi_v6 = bmi_v6/count_v6
bmi_v7 = bmi_v7/count_v7
bmi_v8 = bmi_v8/count_v8
bmi_v9 = bmi_v9/count_v9
bmi_v10 = bmi_v10/count_v10
bmi_v11 = bmi_v11/count_v11
bmi_v12 = bmi_v12/count_v12
bmi_v13 = bmi_v13/count_v13
bmi_v14 = bmi_v14/count_v14
bmi_v15 = bmi_v15/count_v15

print("Average BMI of VB  climber: ", bmi_vb, "  (from ", count_vb, " climbers)")
print("Average BMI of V0  climber: ", bmi_v0, "  (from ", count_v0, " climbers)")
print("Average BMI of V1  climber: ", bmi_v1, "  (from ", count_v1, " climbers)")
print("Average BMI of V2  climber: ", bmi_v2, "  (from ", count_v2, " climbers)")
print("Average BMI of V3  climber: ", bmi_v3, "  (from ", count_v3, " climbers)")
print("Average BMI of V4  climber: ", bmi_v4, "  (from ", count_v4, " climbers)")
print("Average BMI of V5  climber: ", bmi_v5, "  (from ", count_v5, " climbers)")
print("Average BMI of V6  climber: ", bmi_v6, "  (from ", count_v6, " climbers)")
print("Average BMI of V7  climber: ", bmi_v7, "  (from ", count_v7, " climbers)")
print("Average BMI of V8  climber: ", bmi_v8, "  (from ", count_v8, " climbers)")
print("Average BMI of V9  climber: ", bmi_v9, "  (from ", count_v9, " climbers)")
print("Average BMI of V10 climber: ", bmi_v10, "  (from ", count_v10, " climbers)")
print("Average BMI of V11 climber: ", bmi_v11, "  (from ", count_v11, " climbers)")
print("Average BMI of V12 climber: ", bmi_v12, "  (from ", count_v12, " climbers)")
print("Average BMI of V13 climber: ", bmi_v13, "  (from ", count_v13, " climbers)")
print("Average BMI of V14 climber: ", bmi_v14, "  (from ", count_v14, " climbers)")
print("Average BMI of V15 climber: ", bmi_v15, "  (from ", count_v15, " climbers)")

x_plot = ["VB ", "V0 ", "V1 ", "V2 ", "V3 ", "V4 ", "V5 ", "V6 ", "V7 ", "V8 ", "V9 ", 
          "V10", "V11", "V12", "V13", "V14", "V15"]
y_plot = [bmi_vb, bmi_v0, bmi_v1, bmi_v2, bmi_v3, bmi_v4, bmi_v5, bmi_v6, bmi_v7, bmi_v8,
          bmi_v9, bmi_v10, bmi_v11, bmi_v12, bmi_v13, bmi_v14, bmi_v15]

# Scatter plot
plt.scatter(x_plot, y_plot, s=50)
plt.ylabel('Average Body Mass Index')
plt.xlabel('Climb Difficulty')
plt.show()

