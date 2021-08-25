# Election_Analysis


An analysis of voting data contained in [election_results.csv](/Resources/election_results.csv)


## Overview of Election Audit:

This analysis requested by the Colorado Board of Elections uses a program written with Python to open and read a csv file of election data, analyze the data, and outputs the findings including the winner and county with highest voter turnout in a new [text file](/analysis/election_results.txt) once finished.

## Election-Audit Results:

The analysis shows that our dataset contains voting information for 369,711 votes from 3 counties for 3 candidates.

![output.png](/Resources/output.png)

### 1. Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.

Our [program](/PyPoll_Challenge.py) was able to determine that the dataset contains voting information of **3 counties**, the percentage of the total votes from each county, and the number of actual votes from each county.

- Jefferson: 10.5% (38,855)
- **Denver: 82.8% (306,055)**
- Arapahoe: 6.7% (24,801)

### 2. Which county had the largest number of votes?

- Of the three counties analyzed, **Denver county** has the most number of voters at **306,055** which is **82.8%** of the total.

### 3. Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.

Our program is also able to determine the number of candidates in the election, how many votes the candidates received, and the percentage of the total votes that went to each.

- Charles Casper Stockham: 23.0% (85,213)
- **Diana DeGette: 73.8% (272,892)**
- Raymon Anthony Doane: 3.1% (11,606)


### 4. Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

- Of the three candidates analyzed, **Diana DeGette** won the popular vote with **272,892** votes, which is **73.8%** of the total.

## Election-Audit Summary:

The Election analysis program has been written with a broad spectrum of future purposes in mind. By taking any data set of election data the program can be told where to read data from and what variables that data can be extracted to. This can be done by changing only a few variables like **candidate_name = row[2]** to read from a new data set's columns or locations. The program is written in such a way that there is capacity to sort and add the data of every county in Colorado because the **county_options= []** list can be added to automatically for every county name that is read. The same can be done with the **candidate_options = []** list for every candidate name that is read. The dynamic programming makes this program easily applicable for future use with minimal need to be altered. 
