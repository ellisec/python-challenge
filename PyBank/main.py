# PyBank file

import os
import csv

csvpath = "C:\\Users\\ellis\\Downloads\\budget.csv"

TotalMonths = 0
TotalDollars = 0
Avg = 0.0
MaxProfit = 0
MaxDate = ""
MinProfit = 0
MinDate = ""



with open(csvpath, newline ='') as csvfile:
    budgetdata = csv.reader(csvfile, delimiter =',')
    csv_header = next(budgetdata)
  
    print(csv_header)    

    for row in budgetdata:
        TotalMonths = 1 + TotalMonths
        TotalDollars = TotalDollars + int(row[1])
        Aveg = TotalDollars/TotalMonths

        if (int(row[1]) > MaxProfit):
            MaxProfit = int(row[1])
            MaxDate = row[0]

        if (int(row[1]) < MinProfit):
            MinProfit = int(row[1])
            MinDate = row[0]


print("Financial Analysis")
print("----------------------------------------------------------------------------------------------")
print("Total Months: " + str(TotalMonths))
print("Total: " + str(TotalDollars))
print("Average Change: " + str(Aveg))
print("Greatest Increase in Profits occured on Date: " + MaxDate + " with an amount of " + str(MaxProfit))
print("Greatest Decrease in Profits occured on Date: " + MinDate + " with an amount of " + str(MinProfit))