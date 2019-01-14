import csv
from matplotlib import pyplot as plt

path = r"C:\Users\jeffp\OneDrive\Documents\GitHub\Machine-Learning-Project-1\downloads.txt"
file = open(path)
reader = csv.reader(file)

nextVal = None
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
    print(data[i])

plt.plot(data)
plt.show()




