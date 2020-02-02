#The Data we need to Retrieve

#Modules
#CSV Interpreter
import csv

#OS Modifier
import os

#Path to Election File
electioncsv = os.path.join('Resources', 'election_results.csv')
#Path to Output File
electionresults = os.path.join('analysis', 'election_analysis.txt')


#Open CSV to begin processing
with open(electioncsv, newline='') as election_data:
    # Read and Analyze Data Points from CSV
    file_reader = csv.reader(election_data)

    #Read and Print Header Row
    headers = next(file_reader)
    print(headers)




# 1. Total number of Votes Cast
# 2. A Complete List of candidates who recieved Votes
# 3. Percentage breakdown of votes for each Candidate
# 4. Total number of votes per candidate
# 5. Winner of election based on Popular Vote (Most Votes)
