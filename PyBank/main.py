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
        Avg = TotalDollars/TotalMonths

        if (int(row[1]) > MaxProfit):
            MaxProfit = int(row[1])
            MaxDate = row[0]

        if (int(row[1]) < MinProfit):
            MinProfit = int(row[1])
            MinDate = row[0]


print("Financial Analysis")
print("----------------------------------------------------------------------------------------------")
print(f"Total Months: {str(TotalMonths)}")
print(f"Total: {str(TotalDollars)}")
print(f"Average Change: {str(Avg)}")
print(f"Greatest Increase in Profits occured on Date: {MaxDate} with an amount of {str(MaxProfit)}")
print(f"Greatest Decrease in Profits occured on Date:{MinDate} with an amount of {str(MinProfit)}")

with open("Financial_Analysis.txt","w") as txtfile:
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"------------------\n")
    txtfile.write(f"Total Months: {str(TotalMonths)}\n")
    txtfile.write(f"Average Change: {str(Avg)}\n")
    txtfile.write(f"Total: + str(TotalDollars)\n")
    txtfile.write(f"Greatest Increase in Profits occured on Date: {MaxDate} with an amount of {str(MaxProfit)}\n")
    txtfile.write(f"Greatest Decrease in Profits occured on Date:{MinDate} with an amount of {str(MinProfit)}\n")