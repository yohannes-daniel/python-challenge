# PyBank budget data

import os
import csv

# Set path for file
print(os.path.abspath("."))
csvpath = os.path.join("Resources", "budget_data.csv")

# Make sure the file is on the correct path
print("File path is " + csvpath + "\n")

n_of_months = -1
i = 0
date = []
profits_losses = []
net_PL = 0
with open(csvpath, encoding='UTF-8') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    
    # 1. Loop through the rows to count the total number of months
    for row in csvreader:
        n_of_months += 1
        if n_of_months >= 1:
            date.append(row[0])
            profits_losses.append(row[1])

    # 2. Calculate net total amount of the entire period
    # Used https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
    
    for i in range(0, len(profits_losses)):
        profits_losses[i] = int(profits_losses[i])
        net_PL += profits_losses[i] 
        
    # 3. Calculate changes in Profits/Losses over the entire period and the average of those changes
    change_PL = []
    x = 0
    PL_diff = 0
    
    # Use for loop to add all of the changes in Profit/Losses into a new list
    for x in range(0, len(profits_losses)):
        if x >= 1 and x <= len(profits_losses):
            PL_diff = profits_losses[x] - profits_losses[x - 1]
            change_PL.append(PL_diff)
    avg_change = round(sum(change_PL) / len(change_PL), 2)

    # 4. Find the greatest increase in profits over the entire period
    x = 0
    inc_date = str
    inc_profit = 0
    for x in range(0, len(change_PL)):
        if x == 0:
            inc_profit = change_PL[x]
            inc_date = date[x + 1]
        elif change_PL[x] > inc_profit:
            inc_profit = change_PL[x]
            inc_date = date[x + 1]
        
    # 5. Find the greatest decrease in profits over the entire period
    x = 0
    dec_date = str
    dec_profit = 0
    for x in range(0, len(change_PL)):
        if x == 0:
            dec_profit = change_PL[x]
            dec_date = date[x + 1]
        elif change_PL[x] < dec_profit:
            dec_profit = change_PL[x]
            dec_date = date[x + 1]

    print("Financial Analysis \n")
    print("------------------------------------\n")
    print(f'Total Months: {n_of_months}\n')
    print(f'Total: {net_PL}\n')
    print(f'Average Change: ${avg_change}\n')
    print(f'Greatest Increase in Profits: {inc_date} (${inc_profit})\n')
    print(f'Greatest Decrease in Profits: {dec_date} (${dec_profit})')

    # Text file
    with open("analysis/result_PyBank.txt", 'w') as textfile:
        textfile.write("Financial Analysis \n")
        textfile.write("------------------------------------\n")
        textfile.write(f'Total Months: {n_of_months}\n')
        textfile.write(f'Total: {net_PL}\n')
        textfile.write(f'Average Change: ${avg_change}\n')
        textfile.write(f'Greatest Increase in Profits: {inc_date} (${inc_profit})\n')
        textfile.write(f'Greatest Decrease in Profits: {dec_date} (${dec_profit})')
