#Add Dependencies
import csv
import os
#Assign Variable to File and Path
file_to_load = ('/Users/kaitlynhopkins/Documents/Data Analysis/Resources/election_results.csv')
#Open file to write data
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open Election Results and Read File
#election_data = open(file_to_load, 'r')
with open(file_to_load) as election_data:

    #ToDo: Perform Analysis
    #Read file object with reader function
    file_reader = csv.reader(election_data)
    #print header row to show selction of row
    header = next(file_reader)
    print(header)



  


# Data we need to retrieve
#1. Total number of Votes
#2. List of Candidates who received Votes.
#3. Total votes received for each candidates.
#4. Winner of Election based on populare vote.

