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

# Declare candidate list and an empty dictionary for tracking vote count
# Set initial winning candidate tracking values
candidate_options = []
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Declare county list and an empty dictionary for tracking county turnout.
# Set initial largest county turnout tracking values
county_list = []
county_votes = {}

largest_county_turnout_name = ""
largest_county_turnoutcount = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read and analyze the data here, nested under with Open command
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    headers = next(file_reader)

    # Looping through each row in the CSV file and add to total vote count
    for row in file_reader:
     
        total_votes += 1
        
        # Obtain the county and candidate name from each row
        county_name = row[1]
        candidate_name = row[2]

        # If the county does not match any existing county else increase 1 turnout count
        if county_name not in county_list:
            # Add it to the list of county and begin tracking new county turnout
            county_list.append(county_name)
            county_votes[county_name] = 0

        county_votes[county_name] += 1

        # If the candidate does not match any existing candidate esle increase 1 vote count
        if candidate_name not in candidate_options:
            # Add it to the list of candidates and begin tracking vote count.
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

# Print the results tp screem amd add to the text file.
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-----------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)

    # Print County summary header to screen and add to text file
    county_votes_header = (
        f"\nCounty Votes:\n")
    print(county_votes_header, end="")
    txt_file.write(county_votes_header)

    # Determine the percentage of votes for each county by looping through the county votes dictionary.
    # Iterate through counties.
    for county in county_votes:
        # Retrieve vote count of a county
        county_turnout = county_votes[county]
        county_turnout_percentage = int(county_turnout) / int(total_votes) * 100

        # County turnout results for each count, turnout pct formatted to 1 decimal point, and turnout count
        county_results = (f"{county}: {county_turnout_percentage:.1f}% ({county_turnout:,})\n")

        #  Print county results to the screen and save to text file.
        print(county_results)
        txt_file.write(county_results)

    # Determine largest county turnout while looping through county_votes dictionary
    # Determine if the county turnout is greater than current largest turnout value.
        if (county_turnout > largest_county_turnoutcount):
            
            largest_county_turnoutcount = county_turnout
            largest_county_turnout_name = county

    # Print the largest turnout county name to the screen and save to the text file.
    largest_turnout_summary = (
        f"\n-----------------------------------\n"
        f"Largest County Turnout: {largest_county_turnout_name}\n"
        f"-----------------------------------\n")
 
    print(largest_turnout_summary)
    txt_file.write(largest_turnout_summary)

    # Determine the percentage of votes for each candidate by looping through 
    # the candidate dictionary.
    # Iterate through candidates.
    for candidate in candidate_votes:
       
        votes = candidate_votes[candidate]
        vote_percentage = int(votes) / int(total_votes) * 100

        # Calculate candidate results, and format percentage to 1 decimal point.
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        #  Print out candidate results to the screen and save to the text file.
        print(candidate_results)
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate while looping through 
        # candidate_votes dictionary.
        # If true set current candidate votes as winning count, vote pct and winner.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
   
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate

    # Print the winning candidate summary to the screen and save to the text file.
    winning_candidate_summary = (
        f"-----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-----------------------------\n")

    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)






