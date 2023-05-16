# PyPoll budget data

import os
import csv

# Set path for file
print(os.path.abspath("."))
csvpath = os.path.join("Resources", "election_data.csv")

# Make sure the file is on the correct path
print("File path is " + csvpath)

# 1. Calculate the total number of votes
total_votes = -1
ballot_id = []
cand_list = []

# Open election_data
with open(csvpath, encoding='UTF-8') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")

    for row in csvreader:
        total_votes += 1
        if total_votes >= 1:
            ballot_id.append(row[0])
            cand_list.append(row[2])
    
    # 2. A complete list of candidates who received votes
    
    # Create lists for each candidate 
    CCS = []
    DDG = []
    RAD = []
    x = 0
    
    for x in range(0, len(cand_list)):
        if cand_list[x] == "Charles Casper Stockham":
            CCS.append(cand_list[x])
        elif cand_list[x] == "Diana DeGette":
            DDG.append(cand_list[x])
        elif cand_list[x] == "Raymon Anthony Doane":
            RAD.append(cand_list[x])

    # 3. The percentage of votes each candidate won    
    percent_CCS = round((len(CCS) / total_votes), 3) * 100
    percent_DDG = round((len(DDG) / total_votes), 3) * 100
    percent_RAD = round((len(RAD) / total_votes), 3) * 100

    # 4. The total number of votes each candidate won
    total_CCS = len(CCS)
    total_DDG = len(DDG)
    total_RAD = len(RAD)

    # 5. The winner of the election based on popular vote
    winner = str
    if total_CCS > total_DDG and total_CCS > total_RAD: 
        winner = "Charles Casper Stockham"
    elif total_DDG > total_CCS and total_DDG > total_RAD:
        winner = "Diana DeGette"
    elif total_RAD > total_CCS and total_RAD > total_DDG:
        winner = "Raymon Anthony Doane"
    else:
        winner = "A re-election needs to be held."

    print("Election Results \n")
    print("---------------------------------------------------- \n")
    print(f'Total Votes: {total_votes}\n')
    print("---------------------------------------------------- \n")
    print(f'Charles Casper Stockham: {percent_CCS}% ({total_CCS}) \n')
    print(f'Diana DeGette: {percent_DDG}% ({total_DDG}) \n')
    print(f'Raymon Anthony Doane: {percent_RAD}% ({total_RAD}) \n')
    print("----------------------------------------------------\n")
    print(f'Winner: {winner} \n')
    print("----------------------------------------------------")

    # Text file
    with open("analysis/result_PyPoll.txt", 'w') as textfile:
        textfile.write('Elections Results \n')
        textfile.write("------------------------------------\n")
        textfile.write(f'Total Votes: {total_votes}\n')
        textfile.write("---------------------------------------------------- \n")
        textfile.write(f'Charles Casper Stockham: {percent_CCS}% ({total_CCS}) \n')
        textfile.write(f'Diana DeGette: {percent_DDG}% ({total_DDG}) \n')
        textfile.write(f'Raymon Anthony Doane: {percent_RAD}% ({total_RAD}) \n')
        textfile.write("----------------------------------------------------\n")
        textfile.write(f'Winner: {winner} \n')
        textfile.write("----------------------------------------------------")