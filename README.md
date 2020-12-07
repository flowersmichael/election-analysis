# Election Analysis 

## Overview of Election Audit
A Colorado Board of Elections employee has been given the following tasks to complete the election audit of a recent local congressional election.

* How many votes were cast in this congressional election?
* Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
* Which county had the largest number of votes?
* Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
* Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

## Resources
* Data Source: election_results.csv
* Software: Python 3.7.6, Visual Studio Code 1.51.1

## Election-Audit Results
* How many votes were cast in this congressional election?  
369,711

* Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
Jefferson County: 10.5% (38,855).  
Denver County: 82.8% (306,055). 
Arapahoe County: 6.7% (24,801). 

* Which county had the largest number of votes?
Denver

* Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
Charles Casper Stockham: 23.0% (85,213)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.1% (11,606)

* Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
Winner: Diana DeGette
Winning Vote Count: 272,892
Winning Percentage: 73.8%

![Screenshot of text file](https://github.com/flowersmichael/election-analysis/blob/main/Resources/Screen%20Shot%202020-12-06%20at%209.36.21%20PM.png)


## Election-Audit Summary
Thanks to the Colorado Board of Elections for this opportunity to audit the recent 1st District of Colorado, United States House of Representatives election results. The subject of election fraud is unfortunately all over the news today, and election security is as important as ever for the preservation of our democracy. As such, there's a good chance that election audits will be in more demand in future elections.

This code could easily be used for a similar analysis of future 1st District of Colorado elections. More importantly, however, it would be relatively straightforward to adapt this script in other ways as well. For example, rather than county-level data, if provided a precinct-level dataset the script could show candidate results by precinct. Or moving in the other direction, the script could be modified to work with a state-level dataset in, for example, a U.S. Presidential election. The script could then calculate the winner of each state, and with each state's electoral vote number, could be used to determine the U.S. President-elect.
