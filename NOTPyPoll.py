# The data we need to retrieve
# The total number of votes cast.
# Comeplete list of candidates who received votes
# Percentage of votes each candidate won
# Total number of votes each candidate won 
# The winner of the election based on popluar vote.

import csv
import os

# Assign a variable for the file load and path
file_to_load = os.path.join('Resources/election_results.csv')
# Open the election results and read the file.
with open(file_to_load) as election_data:
    
        #Print th file object.
    print(election_data)
    
    # To do: performa analysis.


# Close the file.
election_data.close()


# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# # Using the open() function with the "w" mode we will write data to the file.
# open(file_to_save, "w")

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Using the with statement open the file as a text file.
# outfile = open(file_to_save, "w")
# # Write some data to the file.
# outfile.write("Hello World")

# # Close the file
# outfile.close()

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Hello World \n" )
     # Write three counties to the file.
    txt_file.write("Arapahoe, ")
    txt_file.write("Denver, ")
    txt_file.write("Jefferson, ",)

    # Write three counties to the file.
    txt_file.write("Arapahoe,\nDenver,\nJefferson")

