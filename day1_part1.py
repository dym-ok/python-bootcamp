from itertools import pairwise


with open("day1_input.txt") as f:
    num_increases = 0
    for prev, curr in pairwise(f.readlines()):
        if int(prev) < int(curr):
            num_increases += 1

    print(f"Number of increases: {num_increases}")
