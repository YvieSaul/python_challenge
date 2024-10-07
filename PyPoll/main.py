# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os



# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidates = [] # all candidates
candidate_Vote_Count = {} # candidate vote count

# Winning Candidate and Winning Count Tracker
winner = " " # winning candidate
win_count = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.DictReader(election_data)

   
    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        
                                 
                    
        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = (row["Candidate"])

        # If the candidate is not already in the candidate list, add them
        
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidate_Vote_Count[candidate_name] = 0

        # Add a vote to the candidate's count
        candidate_Vote_Count[candidate_name] += 1
  

election_results = f"\nElection Results\n"
election_results += f"----------------------------------------------------\n"
election_results += f"Total Votes: {total_votes}\n"
election_results += f"----------------------------------------------------\n"

# Loop through the candidates to determine vote percentages and identify the winner
for candidate in candidates:

        # Get the vote count and calculate the percentage
    vote_count = candidate_Vote_Count[candidate]

    vote_percent = (vote_count) / (total_votes) * 100

    election_results += (f"{candidate}: {vote_percent:.3f}% ({vote_count})\n"
)

 # Update the winning candidate if this one has more votes
    if vote_count > win_count:
        win_count = vote_count
        winner = candidate

election_results += f"----------------------------------------------------\n"
election_results += f"Winner: {winner}\n"
election_results += f"-----------------------------------------------------\n"


# Print Output
print(election_results)

with open(file_to_output, "w") as txt_file:
    txt_file.write(election_results)



