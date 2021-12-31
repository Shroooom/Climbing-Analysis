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
print(header)

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
file1 = open('ascent100k.csv', encoding="utf8")
csvreader1 = csv.reader(file1)

header1 = []
header1 = next(csvreader1)
header1 = [header1[1], header1[2]]
print(header1)

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
user_bmi = {}
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
    x_points.append(int(climber[1]))
    y_points.append(user_bmi.get(climber[0]))

# Scater plot o
plt.scatter(x_points, y_points, s=20, alpha= .01)
plt.ylabel('Body Mass Index')
plt.xlabel('Climb Difficulty')
plt.axis([0, 86, 8, 35])
plt.show()



