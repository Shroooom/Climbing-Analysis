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
# file1 = open('ascent100k.csv', encoding="utf8")
file1 = open('ascent750k.csv', encoding="utf8")
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


########## average BMI vs grade sent ##########

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
bmi_v = [float(0),0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
count_v = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for gradedIndex in range(len(x_points)):
    ### grade_id 0-16   VB
    if x_points[gradedIndex]<=16:                                  
        bmi_v[0] = bmi_v[0]+y_points[gradedIndex]
        count_v[0] = count_v[0]+1
    ### grade_id 17-28  V0
    elif x_points[gradedIndex]>=17 and x_points[gradedIndex]<=28:  
        bmi_v[1] = bmi_v[1]+y_points[gradedIndex]
        count_v[1] = count_v[1]+1
    ### grade_id 29-32  V1
    elif x_points[gradedIndex]>=29 and x_points[gradedIndex]<=32:  
        bmi_v[2] = bmi_v[2]+y_points[gradedIndex]
        count_v[2] = count_v[2]+1
    ### grade_id 33-35  V2
    elif x_points[gradedIndex]>=33 and x_points[gradedIndex]<=35:  
        bmi_v[3] = bmi_v[3]+y_points[gradedIndex]
        count_v[3] = count_v[3]+1
    ### grade_id 36-38  V3
    elif x_points[gradedIndex]>=36 and x_points[gradedIndex]<=38:  
        bmi_v[4] = bmi_v[4]+y_points[gradedIndex]
        count_v[4] = count_v[4]+1    
    ### grade_id 39-42  V4
    elif x_points[gradedIndex]>=39 and x_points[gradedIndex]<=42:  
        bmi_v[5] = bmi_v[5]+y_points[gradedIndex]
        count_v[5] = count_v[5]+1
    ### grade_id 43-46  V5
    elif x_points[gradedIndex]>=43 and x_points[gradedIndex]<=46:  
        bmi_v[6] = bmi_v[6]+y_points[gradedIndex]
        count_v[6] = count_v[6]+1
    ### grade_id 47-50  V6
    elif x_points[gradedIndex]>=47 and x_points[gradedIndex]<=50:  
        bmi_v[7] = bmi_v[7]+y_points[gradedIndex]
        count_v[7] = count_v[7]+1
    ### grade_id 51-52  V7
    elif x_points[gradedIndex]>=51 and x_points[gradedIndex]<=52:  
        bmi_v[8] = bmi_v[8]+y_points[gradedIndex]
        count_v[8] = count_v[8]+1   
    ### grade_id 53-55  V8
    elif x_points[gradedIndex]>=53 and x_points[gradedIndex]<=55:  
        bmi_v[9] = bmi_v[9]+y_points[gradedIndex]
        count_v[9] = count_v[9]+1
    ### grade_id 56-58  V9
    elif x_points[gradedIndex]>=56 and x_points[gradedIndex]<=58:  
        bmi_v[10] = bmi_v[10]+y_points[gradedIndex]
        count_v[10] = count_v[10]+1
    ### grade_id 59-60  V10
    elif x_points[gradedIndex]>=59 and x_points[gradedIndex]<=60:  
        bmi_v[11] = bmi_v[11]+y_points[gradedIndex]
        count_v[11] = count_v[11]+1
    ### grade_id 61-63  V11
    elif x_points[gradedIndex]>=61 and x_points[gradedIndex]<=63:  
        bmi_v[12] = bmi_v[12]+y_points[gradedIndex]
        count_v[12] = count_v[12]+1
    ### grade_id 64-65  V12
    elif x_points[gradedIndex]>=64 and x_points[gradedIndex]<=65:  
        bmi_v[13] = bmi_v[13]+y_points[gradedIndex]
        count_v[13] = count_v[13]+1
    ### grade_id 66-67  V13
    elif x_points[gradedIndex]>=66 and x_points[gradedIndex]<=67:  
        bmi_v[14] = bmi_v[14]+y_points[gradedIndex]
        count_v[14] = count_v[14]+1
    ### grade_id 68-69  V14
    elif x_points[gradedIndex]>=68 and x_points[gradedIndex]<=69:  
        bmi_v[15] = bmi_v[15]+y_points[gradedIndex]
        count_v[15] = count_v[15]+1
    ### grade_id 70+    V15
    elif x_points[gradedIndex]>=70:                                   
        bmi_v[16] = bmi_v[16]+y_points[gradedIndex]
        count_v[16] = count_v[16]+1
    else:
        print("you will never see this")

# divide total/count to get average
for i in range(17):
    bmi_v[i] = bmi_v[i]/count_v[i]


#  axis for graphing and printing
x_plot = ["VB", "V0", "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", 
          "V10", "V11", "V12", "V13", "V14", "V15"]
y_plot = [bmi_v[0], bmi_v[1], bmi_v[2], bmi_v[3], bmi_v[4], bmi_v[5], bmi_v[6], bmi_v[7], bmi_v[8], bmi_v[9],
          bmi_v[10], bmi_v[11], bmi_v[12], bmi_v[13], bmi_v[14], bmi_v[15], bmi_v[16]]

# print statements
for i in range(17):
    print("Average BMI of ", x_plot[i], " climber: ", "%.3f" % bmi_v[i], "  (from ", count_v[i], " climbers)")

# find line of best fit 
# following formula: slope = sum((x-x_a)(y-y_a))/sum((x-x_a)^2)
#   and y_a = a(x_a) + b 
xvar = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
yvar = y_plot
x_a = 0
y_a = 0
for i in xvar:
    x_a = x_a+i
x_a =  x_a/17
for i in yvar:
    y_a = y_a+i
y_a =  y_a/17

diffxx_a = []
diffyy_a = []
for i in range(17):
    diffxx_a.append(xvar[i]-x_a)
    diffyy_a.append(yvar[i]-y_a)

multDenom = []
multNumer = []
for i in range(17):
    multDenom.append(diffxx_a[i]*diffxx_a[i])
    multNumer.append(diffxx_a[i]*diffyy_a[i])

sumMultDenom = 0
sumMultNumer = 0
for i in range(17):
    sumMultDenom = sumMultDenom + multDenom[i]
    sumMultNumer = sumMultNumer + multNumer[i]

slope = sumMultNumer/sumMultDenom
yintercept = y_a-(slope*x_a)
yend = (slope*17)+yintercept

slope = round(slope,2)
yintercept = round(yintercept,2)
lineLabel = "y = " + str(slope) + "x + " + str(yintercept)
print(lineLabel)
# draw line of best fit
plt.plot([0,16], [yintercept,yend], color = 'red', label="line of best fit: " + lineLabel)
plt.legend(loc="upper right")

# plot Scatter
plt.scatter(x_plot, y_plot, s=50)
plt.ylabel('Average Body Mass Index')
plt.xlabel('Climb Difficulty')
plt.show()

