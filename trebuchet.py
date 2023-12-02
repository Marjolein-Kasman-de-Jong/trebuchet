# Get input and convert every line into a list item

puzzle_input = []

with open('puzzle_input.txt') as file_object:
    for line in file_object:
        puzzle_input.append(line)

# Convert spelled out numbers to numbers

edited_puzzle_input = []

for input in puzzle_input:
    new_input = input
    if "one" in new_input:
        new_input = new_input.replace("one", "one1one") # I got the idea to replace "one" with "one1one" instead of "1" from Anhuman Dash (https://www.youtube.com/watch?v=iM3fuRrPAzY)
    if "two" in new_input:
        new_input = new_input.replace("two", "two2two")
    if "three" in new_input:
        new_input = new_input.replace("three", "three3three")
    if "four" in new_input:
        new_input = new_input.replace("four", "four4four")
    if "five" in new_input:
        new_input = new_input.replace("five", "five5five")
    if "six" in new_input:
        new_input = new_input.replace("six", "six6six")
    if "seven" in new_input:
        new_input = new_input.replace("seven", "seven7seven")
    if "eight" in new_input:
        new_input = new_input.replace("eight", "eight8eight")
    if "nine" in new_input:
        new_input = new_input.replace("nine", "nine9nine")
    edited_puzzle_input.append(new_input)    
                    
print(edited_puzzle_input)

# Remove letters from list items

puzzle_input_without_letters = []

for item in edited_puzzle_input:
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