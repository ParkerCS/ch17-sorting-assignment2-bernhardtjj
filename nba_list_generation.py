"""
This code was used to produce the randomized NBA list.
It is NOT part of the assignment, but you can look at it
to see how I got the shuffled list if you like.
"""

import random
import re


# This function takes in a line of text and returns
# a list of words in the line.
def split_line(lin):
    return re.findall('[A-Za-z0-9]+(?:\'[A-Za-z0-9]+)?', lin)


file = open("nba_scoring_leaders.csv", "r")
nba_leader_list = []

for line in file:
    line_list = split_line(line)
    name = ""
    for i in range(len(line_list) - 1):
        name += line_list[i]
        if i < (len(line_list) - 2):
            name += " "
    leader = [name, int(line_list[-1])]
    nba_leader_list.append(leader)
print(nba_leader_list)
random.shuffle(nba_leader_list)
print(nba_leader_list)
file.close()
