# Author: JoTing Wong

import os
import csv

# locate file 
file_path = os.path.join("Resources", "budget_data.csv")


with open(file_path, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvfile)
    # print(f"Header: {csv_header}")

    TotalMonth = []
    Total = []
    Change = []
        
    for row in csvreader:

        # Create a list inserting date information
        TotalMonth.append(row[0])
        # Create a list inserting Total information
        Total.append(float(row[1]))
        

    # loop from second row to calculate change between months
    for i in range(1,len(Total)):

        Change.append(Total[i] - Total[i-1])
        AvgChange = sum(Change)/len(Change) 
        MaxChange = max(Change)
        MinChange = min(Change)
        # use list index to identify month information matches to the Max/Min Change
        MaxMonth = TotalMonth[Change.index(max(Change))+1]
        MinMonth = TotalMonth[Change.index(min(Change))+1]

# Print final output in terminal
print("Financial Analysis")
print("-----------------------------------")
print("Total Months: " + str(len(TotalMonth)))
print("Total: $"+str(round(sum(Total))))
print("Average Change: $" + str(round(AvgChange,2))) 
print("Greatest Increase in Profits: " + MaxMonth + " ($" + str(round(MaxChange)) + ")")
print("Greatest Decrease in Profits: " + MinMonth + " ($" + str(round(MinChange)) + ")")


# Save output to text file
output = ["Financial Analysis \n",
            "----------------------------------- \n",
            "Total Months: " + str(len(TotalMonth)) + " \n",
            "Total: $"+str(round(sum(Total))) + " \n",
            "Average Change: $" + str(round(AvgChange,2)) + " \n", 
            "Greatest Increase in Profits: " + MaxMonth + " ($" + str(round(MaxChange)) + ") \n",
            "Greatest Decrease in Profits: " + MinMonth + " ($" + str(round(MinChange)) + ") \n"
            ]


outputFile = open("Financial_Analysis.txt","w") 
outputFile.writelines(output)
outputFile.close()
        

