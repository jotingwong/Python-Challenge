# Author: JoTing Wong

import os
import csv 

# locate file 
file_path = os.path.join("Resources","election_data.csv")


with open(file_path, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvfile)
    # print(f"Header: {csv_header}")

    Candidate = []
        
    for row in csvreader:
        # create a list using candidate column
        Candidate.append(row[2])

#Total Votes 
TotalVote = len(Candidate)

# Total Votes by candidate
TotalK = Candidate.count("Khan")
TotalC = Candidate.count("Correy")
TotalL = Candidate.count("Li")
TotalO = Candidate.count("O'Tooley")

# Percentage of Votes by candidate
PctKhan = (TotalK/TotalVote) * 100
PctCorry = (TotalC/TotalVote) * 100
PctLi = (TotalL/TotalVote) * 100
PctOTooley = (TotalO/TotalVote) * 100  

# Insert the total votes by candidate into a list
PopularVote = [TotalK,TotalC,TotalL,TotalO]

# get the list index with largest total
WinnerIndex = PopularVote.index(max(PopularVote))

# use the list index to identify candidate
if WinnerIndex == 0:
    Winner = "Khan"
elif WinnerIndex == 1:
    Winner = "Corrrey"
elif WinnerIndex == 2:
    Winner = "Li"
elif WinnerIndex == 3:
    Winner = "O'Tooley"



# Print final Output in terminal
print("Election Results")
print("-----------------------------------")
print("Total Votes: " + str(TotalVote))
print("-----------------------------------")
print("Khan: "+ str(round(PctKhan,3)) + "% (" + str(TotalK) + ")")
print("Correy: "+ str(round(PctCorry,3)) + "% (" + str(TotalC) + ")")
print("Li: "+ str(round(PctLi,3)) + "% (" + str(TotalL) + ")")
print("O'Tooley: "+ str(round(PctOTooley,3)) + "% (" + str(TotalO) + ")")
print("-----------------------------------")
print("Winner: " + Winner)

# save output to text file
output = ["Election Results \n",
            "----------------------------------- \n",
            "Total Votes: " + str(TotalVote) + " \n",
            "----------------------------------- \n",
            "Khan: "+ str(round(PctKhan,3)) + "% (" + str(TotalK) + ") \n", 
            "Correy: "+ str(round(PctCorry,3)) + "% (" + str(TotalC) + ") \n",
            "Li: "+ str(round(PctLi,3)) + "% (" + str(TotalL) + ") \n",
            "O'Tooley: "+ str(round(PctOTooley,3)) + "% (" + str(TotalO) + ") \n",
            "----------------------------------- \n",
            "Winner: " + Winner + " \n"
            ]


outputFile = open("Voting_Analysis.txt","w") 
outputFile.writelines(output)
outputFile.close()
        

