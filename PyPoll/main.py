import os
import csv

# CSV file path
election_data_load = "C:/Users/josep/ucf/homework/03-python/python-challenge/PyPoll/Resources/election_data.csv"

#Set the output of the text file
election_analysis_output = os.path.join("analysis", "election_analysis.txt")

#Variables
vote_count = 0
candidates_list = []
candidate_votes = {}
winner_count = 0
winner = ""

#Open csv
with open(election_data_load) as poll_data:
  reader = csv.reader(poll_data)
  ED = next(reader)

  #Loop through to find total votes
  for row in reader:

    #Count number of votes
      vote_count += 1

      candidate = row[2]

    #If statement to run on first time a name appears
      if candidate not in candidates_list:
          candidates_list.append(candidate)
          candidate_votes[candidate] = 0
      
      candidate_votes[candidate] = candidate_votes[candidate] + 1
  
   

# Printing the results
with open(election_analysis_output, 'w') as file:
    #Print to txt file
    file.write("Election Results\n")
    file.write("----------------------------\n")
    file.write(f"Total Votes: {vote_count:,}\n")
    file.write("----------------------------\n")

    #Print to terminal
    print("Election Results\n")
    print("----------------------------\n")
    print(f"Total Votes: {vote_count:,}\n")
    print("----------------------------\n")

    for candidate in candidate_votes:
        votes = candidate_votes[candidate] 
        vote_percentage = float(votes)/float(vote_count)*100
        if (votes > winner_count):
            winner_count = votes
            winner = candidate
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"

        #Print to terminal
        print(voter_output)

        #Print to txt file
        file.write(voter_output)
        

    winning_summary = (f"Winner: {winner}")

    #Print to terminal
    print("----------------------------\n")
    print(winning_summary)
    print("----------------------------\n")

    #Print to txt file
    file.write("----------------------------\n")
    file.write(winning_summary)
    file.write("----------------------------\n")



  


  