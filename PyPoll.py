from pathlib import Path
import csv
file_path= "Starter_Code/PyPoll/Resources/election_data.csv"

with open(file_path, newline='', encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    print(header)

next(csvreader)
data = list(csvreader)
row_count = len(data)

#Create new list from CSV, to get complete list of candidate who recieved votes
candilist = list()
tally = list()
for i in range (0,row_count):
    candidate = data[i][2]
    tally.append(candidate)
        candilist.append(candidate)
candicount = len(candilist)

#total number of votes for each candidate won & percentages
votes = list()
percentage = list()
for j in range (0,candicount):
    votepercentage = cotes[j]/row_count
    percentage.append(votepercentage)

#the winner of election 
winner = votes.index(max(votes))



