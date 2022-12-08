# import required packages
import numpy as np
import pandas as pd
import sys

# import the input data, making sure to retain the blank lines which separate the groups
Day1 = pd.read_csv('Day1.txt', skip_blank_lines=False, header=None, names=["Calories"])

# generate a list of breaks based on NaN lines
breaks = Day1.Calories.isna()

# apply the breaks to Day1 list to generate a list representing each elf
Elves=Day1[~breaks].groupby(breaks.cumsum()).Calories.apply(list).tolist()

# add up the values in each list to see how many caloires each elf is carrying
totals=[sum(i) for i in Elves]

# print the largest sum value representing the greatest amount of calories a single elf is carrying
print(max(totals))

# sort the list of total calories per elf in descending order
totals.sort(reverse=True)

# print the top 3 calorie totals
print(sum(totals[:3]))

