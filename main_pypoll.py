# First we will import the os module
import os
# module for reading CSV files
import csv

with open('Resource/election_data.csv','r') as csvfile:
    csvreader = csv.DictReader(csvfile)

    total_number = 0
    candidates_dict = {}
    candidates_percent = {}

    for row in csvreader:
        total_number = total_number + 1
        if row['Candidate'] not in candidates_dict.keys():
            candidates_dict[row['Candidate']] = 1
        else:
            candidates_dict[row['Candidate']] = candidates_dict[row['Candidate']] + 1

    for candidate in candidates_dict:
        candidates_percent[candidate] = round(candidates_dict[candidate] * 100 / total_number)

    max_votes = 0
    winner = ''
    for candidate in candidates_dict:
        if candidates_dict[candidate] > max_votes:
            max_votes = candidates_dict[candidate]
            winner = candidate

    import sys

    old_sysout = sys.stdout
    sys.stdout = open("analysis/pypoll.txt",'w')

    print("Election Results")
    print("-"*10)
    print("Total Votes: %d"%total_number)
    print("-"*10)
    for candidate in candidates_percent:
        print(candidate + ":" + "%.3f (%d)"%(candidates_percent[candidate],candidates_dict[candidate]))
    print("-"*10)
    print("Winner: %s"%winner)
    print("-"*10)

    sys.stdout = old_sysout







