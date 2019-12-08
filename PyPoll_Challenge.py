# For the election results data file, the client requires calculations for:
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. A complete list of counties and their turnout
# 4. The percentage of turnout for each county
# 5. The turnout count for each county
# 6. The county that has the largest turnout
# 7. The percentage of votes each candidate won
# 8. The total number of votes each candidate won
# 9. The winner of the election based on popular vote


# Import dependencies required for the analysis
import os
import csv
# Assign a variable for the file to load and the path
file_to_load = os.path.join('Resources','election_results.csv')
# Assign a variable to save the file to a path
file_to_save = os.path.join('Analysis','election_analysis_challenge.txt')

# Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []
# Declare the empty dictionary for tracking candidate vote count
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# County list
county_list = []
# Declare the empty dictionary for tracking county turnout
county_votes = {}

# Largest County Turnout
largest_county_turnout_name = ""
largest_county_turnoutcount = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read and analyze the data here, nested under with Open command
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    # Read the header row.
    headers = next(file_reader)

    # Looping through each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        
        # Obtain the county and candidate name from each row
        county_name = row[1]
        candidate_name = row[2]

        # If the county does not match any existing county
        if county_name not in county_list:
            # Add it to the list of county.
            county_list.append(county_name)

            # Begin tracking that county turnout count.
            county_votes[county_name] = 0

        # Add a vote to that county's turnout count.
        county_votes[county_name] += 1

        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Save the results to the text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-----------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Add County summary header
    county_votes_header = (
        f"\nCounty Votes:\n")

    print(county_votes_header, end="")
    # Save the county summary header to the text file
    txt_file.write(county_votes_header)

    # Determine the percentage of votes for each county by looping through the county votes dictionary.
    # Iterate through counties.
    for county in county_votes:
        # Retrieve vote count of a county
        county_turnout = county_votes[county]
        # Calculate the percentage of turnout.
        county_turnout_percentage = int(county_turnout) / int(total_votes) * 100

        # County turnout results for each count, turnout pct formatted to 1 decimal point, and turnout count
        county_results = (f"{county}: {county_turnout_percentage:.1f}% ({county_turnout:,})\n")

        #  Print out county results 
        print(county_results)
        #  Save the county results to the text file.
        txt_file.write(county_results)

    # Determine largest county turnout while looping through county_votes dictionary
    # Determine if the county turnout is greater than current largest turnout value.
        if (county_turnout > largest_county_turnoutcount):
            # If true then reset largest turnoutcount to current county turnout count
            largest_county_turnoutcount = county_turnout
            # And, reset the largest turnout county name to current county
            largest_county_turnout_name = county

    # Print the largest turnout county name to the terminal
    largest_turnout_summary = (
        f"\n-----------------------------------\n"
        f"Largest County Turnout: {largest_county_turnout_name}\n"
        f"-------------------------------------\n")
 
    # Save the Largest Turnout to text file
    txt_file.write(largest_turnout_summary)

    # Determine the percentage of votes for each candidate by looping through 
    # the candidate dictionary.
    # Iterate through candidates.
    for candidate in candidate_votes:
        # Retrive vote count of a candidate
        votes = candidate_votes[candidate]
        # Calculate the percentage of votes.
        vote_percentage = int(votes) / int(total_votes) * 100

        # Calculate candidate results, and format percentage to 1 decimal point.
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        #  Print out candidate results to the terminal.
        print(candidate_results)

        #  Save the candidate results to the text file.
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate while looping through 
        # candidate_votes dictionary.
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning count = votes and winning pct = vote pct
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name
            winning_candidate = candidate

    # Print the winning candidate summary to the terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    # print(winning_candidate_summary)
    # save the winning candidate's results to the text file
    txt_file.write(winning_candidate_summary)






