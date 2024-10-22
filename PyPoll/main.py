# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
load_file = os.path.join("Resource", "election_data.csv")  # Input file path
load_output = os.path.join("Analysis", "ElectionAnalysis.txt")  # Output file path


# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
win_votes = 0
win_percent = 0
win_candidate = 0


# Define lists and dictionaries to track candidate names and vote counts
candidates = ""
candidates_votes = {}

# Winning Candidate and Winning Count Tracker


# Open the CSV file and process it
with open(load_file) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for read in reader:

        #total number of votes
        total_votes += 1
        #get candidate name from each row
        candidate = read[2]
#       # If the candidate is not already in the candidate list, add them
        if candidate in candidates_votes: #if any of the candidate names have not already been added to the list of candidates, then add them
            candidates_votes[candidate] += 1 #Add a vote to the candidate's count
        else:    
            candidates_votes[candidate] = 1
        
with open(load_output, "w") as txt_file: #print into text file

        election_total = (f"Election Results\n"
                          f"\n"
                          f"-------------------------\n"
                          f"\n"
                          f" Total Votes: {total_votes}"
                          f"\n"
                          f"\n"
                          f"-------------------------\n"
                          f"\n") 
        txt_file.write(election_total) 



with open(load_output, "a") as txt_file: #print into text file without overwritting pervious outputs: find this on google AI generated answer

    for candidate in candidates_votes:
        votes = candidates_votes.get(candidate) #grabbing total votes per candidate to find the percentaes
        percentage = float(votes) / float(total_votes) * 100
        results = f"{candidate}: {percentage: .3f}% ({votes})" #.3f means to round to the nearest 3rd decimal
        election_results = (f"{results}\n"
                            f"\n")
        txt_file.write(election_results)


        if (votes > win_votes) and (percentage > win_percent):
            win_votes = votes
            win_percent = percentage
            win_candidate = candidate
    winner = (f"\n"
              f"-------------------------\n"
              f"\n"
              f" Winner: {win_candidate}\n"
              f"\n"
              f"-------------------------\n")
    txt_file.write(winner)


