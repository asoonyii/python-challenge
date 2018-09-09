#Onyinyechi Asoluka
#Python homework2- PyPoll
#8th September 2018
import os
import csv

#Collect data
csvpath= os.path.join("election_data.csv")
# Set initial counters, candidates, and winners
total_votes = 0
unique_candidate_list = []
candidate_vote = {}
count_winner= 0

# Read the csv and account for header
with open(csvpath,'r') as csvfile:
    csvlines = csv.reader(csvfile, delimiter=',')
    csvheader= next(csvlines)

    # Loop through rows
    for row in csvlines:
        # Get total votes by counting rows
        total_votes = total_votes + 1

        # Get list of named candidates
        candidatename = row[2]

        # Get list of unique candidates and add to candidate list
        if candidatename not in unique_candidate_list:
            unique_candidate_list.append(candidatename)

            # Get the candidate vote list for each candidate
            candidate_vote[candidatename] = 0
        candidate_vote[candidatename] = candidate_vote[candidatename] + 1

with open("main.txt", "w") as textfile:
    #Put result and vote on terminal and text file
    print("")
    print("Election Results")
    print("--------------------")
    print("Total Votes: "+str(total_votes))
    print("----------------------")
    textfile.write("")
    textfile.write("\nElection Results")
    textfile.write("\n--------------------")
    textfile.write("\nTotal Votes: "+ str(total_votes))
    textfile.write("\n-----------------------\n")

    for candidate in candidate_vote:
        # calculates vote and percentage and winner
        votes = candidate_vote.get(candidate)
        percent= (votes) / (total_votes) * 100
        if (votes > count_winner):
            count_winner = votes
            winner = candidate

        candidate_all = f"{candidate}: {percent:.3f}% ({votes})\n"
        print(candidate_all)
        textfile.write(candidate_all)

    print("--------------------")
    print("Winner: " + winner)
    print("--------------------")
    textfile.write("\n--------------------")
    textfile.write("\nWinner: " + winner)
    textfile.write("\n--------------------")
