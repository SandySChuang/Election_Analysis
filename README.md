# Election_Analysis
## Project Overview
A Colorado Board of Elections employee has given me the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software:  Python 3.8.0, Visual Studio Code 1.40.2

## Summary
The analysis of the election shows that:
- There were 369,711 votes cast in the election
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 votes
  - Diane DeGette received 73.8% of the vote and 272,892 votes
  - Ramon Anthony Doane received 3.1% of the vote and 11,606 votes
- The winner of the election was
  - Diane DeGette who received 73.8% of the vote and 272,892 votes
  
## Challenge 3 Overview
For the challenge, the PyPoll codes need to be refactored to include calculations for each county's voting turnout counts and percentages.  From the county results, the client also needs to know the county with the largest turnout for this local election.  These county summary results are to be added to the Election Analysis output file.
- The refactored codes still only loop through the entire data file only once.
- While going through each row, in addition to the existing if statement that adds new candidate to the candidate list and counting candidate votes, the refactored codes insert another if statement looking at the county name from the ballot record and counting county turnout accordingly.
- The refactored codes add County Vote Summary section and the Largest County Turnout info to the Election Analysis output file.

## Challenge Summary
The analysis of the election now shows that:
- There were 369,711 votes cast in the election
- The counties involved in the election were:
  - Jefferson County
  - Denver County
  - Arapahoe County
- The county votes were:
  - Jefferson: 10.5% (38,855)
  - Denver: 82.8% (306,055)
  - Arapahoe: 6.7% (24,801)
- The largest county turnout was from Denver.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 votes
  - Diane DeGette received 73.8% of the vote and 272,892 votes
  - Ramon Anthony Doane received 3.1% of the vote and 11,606 votes
- The winner of the election was
  - Diane DeGette who received 73.8% of the vote and 272,892 votes
