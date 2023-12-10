from itertools import pairwise
from aocd import get_data

num_increases = 0
data = get_data(day=1, year=2021)
for prev, curr in pairwise(data.splitlines()):
    if int(prev) < int(curr):
        num_increases += 1

print(f"Number of increases: {num_increases}")
