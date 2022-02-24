#Add Dependencies
import csv
import os
#Assign Variable to File and Path
file_to_load = ('/Users/kaitlynhopkins/Documents/Data Analysis/Resources/election_results.csv')
#Open file to write data
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Initialize the total Votes to 0
total_votes = 0
#4. Initialize candidate list variable
candidate_options = []
#8. Initialize dictionary to hold candidate options as keys and votes as values
candidate_votes = {}
#15. Initializing winner data 
winning_candidate = ''
winning_count = 0
winning_percentage = 0

#Open Election Results and Read File
#election_data = open(file_to_load, 'r')
with open(file_to_load) as election_data:

    #ToDo: Perform Analysis
    #Read file object with reader function
    file_reader = csv.reader(election_data)
    #print header row to show selction of row
    header = next(file_reader)

    
    #print each row in file
    for row in file_reader:
        # 2. Increase total votes for each row
        total_votes += 1
       # print(row)
       #5. Collect candidate names from rows
        candidate_name = row[2]
        
        #6. Check to see if name is not in list
        if candidate_name not in candidate_options:
            #7. Add new name to candidate options list
            candidate_options.append(candidate_name)
            #9. set new dictionary key with value of 0
            candidate_votes[candidate_name] = 0

        #10. Add candidate votes after new key is added to dictionary
        candidate_votes[candidate_name] += 1

    
# Data we need to retrieve
#1. Total number of Votes
print(total_votes)
#2. List of Candidates who received Votes.
print(candidate_options)
#3. Total votes received for each candidates.
print(candidate_votes)
#4. Percentage of Votes Won
#11. Iterate through candidates dictionary
for candidate_name in candidate_votes:
    #12. set value variable to votes for each value in dictionary
    votes = candidate_votes[candidate_name]
    #13. Calculate percentage votes based on each value
    percentage_votes = float(votes) / float(total_votes) * 100
    #14. Display candidate name and perecentage of votes received
    print(f"{candidate_name}: {percentage_votes:.1f}% ({votes:,})\n")
#5. Winner of Election based on populare vote.
    #16. Set the winning total to the highest votes and percentage per candidate
    if (votes > winning_count) and (percentage_votes > winning_percentage):
        winning_count = votes
        winning_percentage = percentage_votes
        #set the the winning candidate to candidate name
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"--------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Coutn: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage: .1f}%\n"
    f"---------------------------\n")
print(winning_candidate_summary)