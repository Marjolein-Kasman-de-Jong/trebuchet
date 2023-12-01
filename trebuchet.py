# Get input and convert every line into a list item

puzzle_input = []

with open('puzzle_input.txt') as file_object:
    for line in file_object:
        puzzle_input.append(line)

# Remove letters from list items

puzzle_input_without_letters = []

for item in puzzle_input:
    new_item = ''.join(filter(str.isdigit, item))
    puzzle_input_without_letters.append(new_item)

# Create list of two-digit strings from puzzle_input_without_letters

two_digit_numbers = []

for item in puzzle_input_without_letters:
    new_item = item[0] + item[-1]
    two_digit_numbers.append(new_item)

# Convert two-digit strings to ints and add up

sum = 0

for item in two_digit_numbers:
    sum += int(item)

print(sum)