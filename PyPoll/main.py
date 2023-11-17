import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")

with open (election_csv, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)

    total_votes = 0
    candidates_votes = {}

    for row in csv_reader:
        total_votes += 1

        candidate = row[2]

        if candidate in candidates_votes:
            candidates_votes[candidate] += 1
        else:
            candidates_votes[candidate] = 1

txt_election = 'analysis/election_results.txt'

with open (txt_election, 'w') as output_file:
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")

    # Write analysis to the text file
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")

    for candidate, votes in candidates_votes.items():
        percentage = (votes / total_votes) * 100
        print(f"{candidate}: {percentage:.3f}% ({votes})")
        output_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    
    winner = max(candidates_votes, key = candidates_votes.get)

    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")
    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------\n")
