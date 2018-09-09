#Onyinyechi Asoluka
#Python homework 1- PyBank
#8th September 2018
import os
import csv
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
    #Calculate the difference between months and store
    for x in range(1, len(data)):
           diffy = (int(data[x])) - int(data[x-1])
           diff.append(diffy)
    #calculate average change and get greatest increase and decrease
    avgchange= round(sum(diff)/(len(diff)),2)
    Greatest_increase = max(diff)
    Greatest_decrease = min(diff)
    #make an index of increase and decrease and get the corresponding month
    month_increase_index= diff.index(Greatest_increase)
    month_decrease_index= diff.index(Greatest_decrease)
    month_increase= month[month_increase_index +1]
    month_decrease= month[month_decrease_index +1]
print("")
print("Financial Analysis")
print("-----------------------")
print("Total months: " , str(nummonth))
print("Total: $"+str(total))
print("Average Change: $", str(avgchange))
print("Greatest Increase in Profits: " , str(month_increase), " ($"+str(Greatest_increase)+")")
print("Greatest Decrease in Profits: ", str(month_decrease), " ($"+str(Greatest_decrease)+")")

with open("main.txt","w") as textfile:
    textfile.write("\n")
    textfile.write("Financial Analysis")
    textfile.write("\n-----------------------")
    textfile.write("\nTotal months: " + str(nummonth))
    textfile.write("\nTotal: $" + str(total))
    textfile.write("\nAverage Change: $"+ str(avgchange))
    textfile.write("\nGreatest Increase in Profits: " + str(month_increase)+ " ($" +str(Greatest_increase)+")")
    textfile.write("\nGreatest Decrease in Profits: "+ str(month_decrease)+ " ($"+ str(Greatest_decrease)+ ")")