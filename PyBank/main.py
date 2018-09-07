import os
import csv
#QUESTIONS:
#Create csv path to get data from pythonstuff folder
csvpath = os.path.join("budget_data.csv")
#Read file
with open(csvpath,'r') as csvfile:
    csvlines= csv.reader(csvfile, delimiter=',')
    #skip first line
    csvheader= next(csvlines)
    #Store initial total and months
    total = 0
    nummonth = 0
    diff= []
    data= []
    month=[]
    #loop through rows
    for row in csvlines:
        #Count number of months using total no of rows
        nummonth= nummonth +1 
        month.append(row[0])
        #Total net amount of Profit/Losses
        total += float(row[1])
        row[1]

        data.append(row[1])
    for x in range(1, len(data)):
           diffy = (int(data[x])) - int(data[x-1])
           diff.append(diffy)
    avgchange= sum(diff)/(len(diff))
    Greatest_increase = max(diff)
    Greatest_decrease = min(diff)
    month_increase_index= diff.index(Greatest_increase)
    month_decrease_index= diff.index(Greatest_decrease)
    month_increase= month[month_increase_index +1]
    month_decrease= month[month_decrease_index +1]
print("Total months: ", str(nummonth))
print("Total: $", str(total))
print(avgchange)
print(Greatest_increase)
print(Greatest_decrease)
print(month_decrease)
print(month_increase)
