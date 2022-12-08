import numpy as np
import scipy as sci
import pandas as pd
import sys

elf = pd.read_csv('Day1.txt', skip_blank_lines=False, header=None, names=["Cal"])

pd.set_option('display.max_rows', elf.shape[0]+1)

g = elf.Cal.isna()
Calories=elf[~g].groupby(g.cumsum()).Cal.apply(list).tolist()
print(Calories)
print(type(Calories))

totals=[sum(i) for i in Calories]

print(max(totals))

totals.sort(reverse=True)
print(totals[:3])

