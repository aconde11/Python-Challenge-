import pandas as pd
from pathlib import Path
import csv
file_path=Path("Starter_code/PyBank/Resources/budget_data.csv")
count=[] #define variables outside of loop
months = 0
total_months = 0
total_profitloss = 0
dates = []
profit = []
profit_total = []
with open(file_path,'r') as data_file:
    reader=csv.reader(data_file)
    next(reader)
    for row in reader:
        print(row)

        print(row)
    #months start at 0 and add 1 to month count per each row of data is csvreader
    months = months + 1  
    #store data for later use in calculations for Increase/Decrease
    dates.append(row[0])
    #store the profit data and calculate the total profit
    profit.append(row[1])
    change = int(row[1])
    value = int(row[1])

    total_months +=1
    total_profitloss = total_profitloss + int(row[1]) #total profit loss over period

    #greatest increase in profits
    greatest_increase = max(profit)
    greatest_index = profit.index(greatest_increase)
    greatest_dates = dates[greatest_index]

    #greatest decrease 
    greatest_decrease = min(profit)
    worst_index = profit.index(greatest_decrease)
    worst_dates = dates[greatest_index]

    #average change in profit/losses between months over period
    avg_change = sum(profit)/len(profit)


   




    


