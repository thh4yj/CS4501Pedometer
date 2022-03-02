from unittest import skip
import csv
dataLocation = input("Enter the name of the file: ")
print("Reading file named: ", dataLocation)
x_avg = []
x_rate = 29
x = []
try:
    # geeksforgeeks csv tutorial
    with open(dataLocation, 'r') as csvfile:
        data = csv.reader(csvfile, delimiter = ',')
        i = -2
        avgx = 0
        for row in data:
            i+=1
            if(i == -1):
                continue
            x.append(float(row[1]))
            avgx += float(row[1])
            if(i % x_rate == 0):
                avgx = avgx / x_rate
                x_avg.append(avgx)
                avgx = 0
    totals = 0
    peaks = 0
    for i in x_avg:
        if(totals > 0):
            if(totals + 1 == len(x_avg)):
                skip
            elif(i > 0.5 and x_avg[totals-1] < i and x_avg[totals+1] < i):
                peaks +=1
        totals += 1
    print("Steps taken: ", peaks * 2)
except:
    print("Error reading file!")