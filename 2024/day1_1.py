from aocd import get_data
from functools import reduce

input_data = get_data(day=1, year=2024)

column1, column2 = zip(
    *map(lambda line: tuple(map(int, line.split())), input_data.splitlines())
)
column1 = sorted(column1)
column2 = sorted(column2)

total_distance = reduce(
    lambda cum_sum, next_pair: cum_sum + abs(next_pair[0] - next_pair[1]),
    zip(column1, column2),
    0,
)

appearance_fq = list(
    map(lambda x: x * len(list(filter(lambda y: y == x, column2))), column1)
)
similarity_score = reduce(
    lambda cum_sum, next_val: cum_sum + next_val, appearance_fq, 0
)
print(total_distance)
print(similarity_score)
