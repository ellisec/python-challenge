# PyBank file

import os
import csv

csvpath = "C:\\Users\\ellis\\Downloads\\budget.csv"

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
def Analysis(fin_data):
    months = int(sum(fin_data[0]))
    total_amount = int(sum(fin_data[1]))
    mon_max = int(max(fin_data[1]))
    mon_min = int(min(fin_data[1]))

    print(f"Total Months: {str(months)}")
    print(f"Total: {str(total_amount)}")
    print(f"Greatest Increase in Profits: {str(mon_max)}")
    print(f"Greatest Decrease in Profits: {str(mon_min)}")
