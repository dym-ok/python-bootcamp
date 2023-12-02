from typing import Iterable


def sum_of_digits(numbers_seq: Iterable[str]):
    """
    Sum the digits in a list of strings representing numbers
    """
    total = 0
    for num in numbers_seq:
        total += int(num.strip())
    return total


with open('day1_input.txt') as f:
    content = f.readlines()
    num_increases = 0
    for i in range(len(content)-3):
        prev_values = content[i:i+3]
        next_values = content[i+1:i+4]
        sum_prev = sum_of_digits(prev_values)
        sum_next = sum_of_digits(next_values)
        if sum_prev < sum_next:
            num_increases += 1

    print(f"Number of window increases: {num_increases}")
