# First we will import the os module
import os
# module for reading CSV files
import csv

with open('Resource/budget_data.csv', newline='\n') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    date = []
    profit_loss= []
    monthly_changes = []

    count = 0
    total_profit_loss = 0
    total_profit_loss_change = 0
    initial_profit_loss = 0

    for row in csvreader:
        date.append(row[0])
        profit_loss.append(int(row[1]))

    count += len(date)
    total_profit_loss = sum(profit_loss)

    for i in range(1,len(profit_loss)):
            monthly_changes.append(profit_loss[i] - profit_loss[i-1])

    average_change = sum(monthly_changes) / (count-1)
    greatest_increase = max(monthly_changes)
    minimum_increase = min(monthly_changes)


    date_max = date[monthly_changes.index(greatest_increase) + 1]
    date_min = date[monthly_changes.index(minimum_increase) + 1]

    import sys

    old_sysout = sys.stdout
    sys.stdout = open("analysis/pybank.txt",'w')

    print(f'Finanacial Analysis')
    print("--------------------------")
    print("Total Months : " +str(count))
    print("Total : $" +str(total_profit_loss))
    print("Average Change : %.2f"%average_change)
    print(f"Greatest Increase in Profit :" + str(date_max) + " ($%f)"%greatest_increase)
    print(f"Greatest Decrease in Profit :" + str(date_min) + " ($%f)"%minimum_increase)

    # Print the output (to terminal)

    # Export the results to text file
    sys.stdout = old_sysout





