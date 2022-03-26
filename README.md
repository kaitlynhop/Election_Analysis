# Election Audit

## Overview of Election Audit
In this project, a CSV file containing election data was analyzed to determine election results. Using Python to analyze election data, the following results were determined:

  1. The total number of votes cast.
  2. The number of votes received by each candidate.
  3. The percentage of votes received by each candidate.
  4. The winner of the election based on the popular vote. 
  5. Voter turnout based on county.
  6. Percentages of votes from each county.
  7. The county with the highest voter turnout. 

### Purpose
The purpose of this project was to automate election data using Python, to quickly sort and generate results.

## Resources
**Data Source:** [Election data](/Resources/election_results.csv)
<br>**Software:** Python 3.10.2 VS code 1.64.2

## Election-Audit Results
- How many votes were cast in this congressional election?
  -   The total votes cast in this congressional election were 369,711.
- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
  -   Votes per County:
  -   Jefferson: 10.5% (38,855)
  -   Denver: 82.8% (306,055)
  -   Arapahoe: 6.7% (24,801) 
- Which county had the largest number of votes?
  -   Denver County had the largest number of votes with 306,055 votes, which was 82.8% of the total votes. 
- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
  -   Charles Casper Stockham: 23.0% (85,213)
  -   Diana DeGette: 73.8% (272,892)
  -   Raymon Anthony Doane: 3.1% (11,606)
- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
  -   The winner of the election was Diana DeGette, with 272,892 votes, which is 73.8% of the votes cast.

## Election-Audit Summary
- Give at least two examples of how this script can be modified to be used for other elections.
  -   The codes used to analyze election results for this congressional election may be easily used to analyze other election data by simply modifying the code to match the location of data in the csv file containing result data. 
    -   1. In lines 47 and 50, "candidate_name = row[2]" and "county_name = row[1]", the numbers reference the columns for candidate names and county names to aggregate and count. These numbers would be modified depending on the column location of a different election set. 
    -   2. Alternatively, functions can be used in python to include the counting operations for specific variables. A function with the paramters of candidate name and county name, would have the code block that counts the number of votes, percentage of votes, and defines the winners. Then the function could be called to display the candidate and county votes per election. 

