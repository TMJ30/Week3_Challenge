# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
load_file = os.path.join("Resources", "budget_data.csv")  # Input file path 
output_file = os.path.join("Analysis", "BudgetAnalysis.txt")  # Output file path


# Define variables to track the financial data when needed: Count Total Months
total_months = 0
monthly_changes = [] #to keep list of the calculated monthly changes..will be used in the highes/lowest change portion
months = []
highest_in = {"month": "", "change": 0}
highest_de = {"month": "", "change": float("inf")}

# Open and read the csv
with open(load_file) as financials: #open the file so that work can be done in the file; "with" closes the file without having to actually write close()
    reader = csv.reader(financials) #python script to read the file

    # Skip the header row
    header = next(reader)

    # Calling the next row after the header has been set
    first_row = next(reader)
    # Create calculations/functions to be used in the loop: Total Month, Total Amt,
    total_months += 1 #another way to say total_months = total_months + 1 --> originally total_months was assigned 0, not it is 1 bc 0+1=1
    total_amt = int(first_row[1]) #selecting the first value in profit/losses column; set up to use in for loop
    previous_change = int(first_row[1]) #selecting the first value in profit/losses column; set up to use in for loop highest and lowest change

    #Create for loop to read through each row and speficied column to get: Total Months, Total Dollar Amt
    for read in reader: #if variable in reader then
        total_months += 1 #should go through each row and count the total number of months or rows in the data
        total_amt += int(read[1]) # reads through each row, reassigns selected aggreagted to total_amt, and adds each aggregated row to the next unaggregated row; another way to write totalamt = totalamt + 1
        current_change = int(read[1]) #read through each row
        
        changes = current_change - previous_change
        previous_change = current_change #rename previous change to capture the latest subtraction results 

        months.append(read[0])
        monthly_changes.append(changes)

        if changes > highest_in["change"]: #if current value of changes is greater than highest change stored in highes_in --> from in class work through
            highest_in["month"] = read[0]
            highest_in["change"] = changes

        if changes < highest_de["change"]:
            highest_de["month"] = read[0]
            highest_de["change"] = changes 


average = round(sum(monthly_changes) / len(monthly_changes),2)

output = (f"Financial Analysis\n" 
          f"\n"
          f"--------------------\n"
          f"\n"
          f"Total Months: {total_months}\n"
          f"\n"
          f"Total: ${total_amt}\n"
          f"\n"
          f"Average Change ${average}\n"
          f"\n"
          f"Greatest Increase in Profits: {highest_in['month']} (${highest_in['change']}) \n" 
          f"\n"
          f"Greatest Increase in Profits: {highest_de['month']} (${highest_de['change']})" )


# Write the results to a text file
with open(output_file, "w") as txt_file:
    txt_file.write(output)
