import csv
import numpy as np
from matplotlib import pyplot as plt

path = r"C:\Users\jeffp\OneDrive\Documents\GitHub\Machine-Learning-Project-1\downloads.txt"
file = open(path)
reader = csv.reader(file)

nextVal = None
sumX = 0
sumY = 0
sumProdXY = 0
sumSqX = 0
sumSqY = 0
numPoints = 0
slope = 0
intercept = 0
maxX = 0
data = []

# populate two dimensional list (data) with entries
for row in reader:
    hour = int(row[0])
    if row[1] != 'nan':
        downloads = int(row[1])
    else:
        downloads = None
    data.append([hour, downloads])

# replace missing values with mean of two adjacent valid values unless it is the first or last valid value
for i in range(len(data)):
    if data[i][1] is None and i != 0 and i != (len(data) - 1) and data[i - 1][1] is not None:
            j = 1
            while data[i + j][1] is None:
                j += 1
                if (i + j) > (len(data) - 1):
                    break
                else:
                    continue
                break
            if (i + j) <= (len(data) - 1):
                nextVal = data[i + j][1]
                data[i][1] = (nextVal + data[i-1][1]) // 2

for i in range(len(data)):
    if data[i][1] is not None:
        curX = data[i][0]
        curY = data[i][1]
        sumX += curX
        sumY += curY
        sumProdXY += curX * curY
        sumSqX += curX ** 2
        sumSqY += curY ** 2
        numPoints += 1
        if data[i][0] > maxX:
            maxX = data[i][0]

slope = ((numPoints * sumProdXY) - (sumX * sumY)) / ((numPoints * sumSqX) - (sumX ** 2))
intercept = (sumY - (slope * sumX)) / numPoints

x = np.array(range(0, maxX))
y = intercept + (slope * x)

print(slope, intercept)
plt.plot(x, y, 'red')
plt.scatter(*zip(*data))
plt.title('Previous Month Downloads')
plt.xlabel('Hour')
plt.ylabel('Downloads')
plt.show()




