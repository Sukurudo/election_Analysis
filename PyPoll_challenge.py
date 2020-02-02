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

#Initalize Vote Tally
total_votes = 0

#Candidate Options
candidate_options = []

#County Options
county_options = []

#candidate Votes Dictionary
candidate_votes = {}

#County Votes Dictionary
county_votes = {}

#initalize winner data
#winner winner chicken dinner
winning_candidate = ""
winning_count = 0
winning_percentage = 0

winning_county = ""
winning_county_count = 0
winning_county_percentage = 0


#Open CSV to begin processing
with open(electioncsv, newline='') as election_data:
    # Read and Analyze Data Points from CSV
    file_reader = csv.reader(election_data)

    #Read and Print Header Row
    headers = next(file_reader)

    #Analyze the rows
    for row in file_reader:
        # 1. Total number of Votes Cast
        total_votes += 1

#Complete List of Counties and number of Votes
        #Add countie names from each row
        county_name = row[1]

        #add unique Counties to county options
        if county_name not in county_options:
            #Add county names to List
            county_options.append(county_name)
            #Track County Votes
            county_votes[county_name] = 0

        #increment County Votes
        county_votes[county_name] += 1


# 2. A Complete List of candidates who recieved Votes

        # Add Candidate Names from each Row
        candidate_name = row[2]

        #Add unique Candidates to Candidate Options
        if candidate_name not in candidate_options:
            #add Candidate names to List
            candidate_options.append(candidate_name)
            #Track individual Candidate Votes
            candidate_votes[candidate_name] = 0

        #Increment Candidate Vote Count
        candidate_votes[candidate_name] += 1

#Open file to save Election Results
with open(electionresults, "w") as txt_file:

    #Headers
    election_results = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n"
    f"\n"
    f"County Votes:\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # County Breakdown of Votes
    for county in county_votes:
        #Retrieve Vote Count
        Cvotes = county_votes[county]
        #Calculate County Vote Percentage
        Cvote_percentage = int(Cvotes) / int(total_votes) * 100

        #Find Highest County Turnout
        if (Cvotes > winning_county_count) and (Cvote_percentage > winning_county_percentage):
            #Set current County as top Performer
            winning_county_count = Cvotes
            winning_county_percentage = Cvote_percentage
            winning_county = county

        #Print County Results
        county_results = (f"{county}: {Cvote_percentage:.1f}% ({Cvotes:,})\n")
        print(county_results)
        txt_file.write(county_results)

    #County Highest Turnout
    winning_county_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {winning_county} "
        f"with {winning_county_percentage:.1f}% of all Votes\n"
        f"-------------------------\n\n")
    print(winning_county_summary)
    txt_file.write(winning_county_summary) 

    candidate_header = ("Candidate Vote Analysis:\n")
    print(candidate_header)
    txt_file.write(candidate_header)

    # 3. Percentage breakdown of votes for each Candidate
    for candidate in candidate_votes:
        #Retrieve vote count
        votes = candidate_votes[candidate]
        #Calculate Percentages
        vote_percentage = int(votes) / int(total_votes) * 100

        #figure out the Winner
        #Is current candidate the Winner?
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #Set current candidate as winner and store data
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate

        #Print Vote Percentages
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)


    # 5. Winner of election based on Popular Vote (Most Votes)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)

