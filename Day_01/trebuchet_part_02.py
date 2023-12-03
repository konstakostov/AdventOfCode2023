# The total sum of the calibration documents
calibration_values_sum = 0

# Max length of the numbers 1-9, spelled
max_length = 5

NUMBERS = [
    ('zero', '0'),
    ('one', '1'),
    ('two', '2'),
    ('three', '3'),
    ('four', '4'),
    ('five', '5'),
    ('six', '6'),
    ('seven', '7'),
    ('eight', '8'),
    ('nine', '9'),
]

# Opening file with puzzle input
with open('trebuchet_input.txt', 'r') as file:
    for line in file:
        # Removing '\n' from the end of each line
        line = line.rstrip()

        # Empty string is created to store the found calibration values
        calibration_value = ""
        # Empty list is created to store all found numbers in the documents
        found_numbers = []

        # Index to prevent infinite loops when number is added
        index = None

        for i in range(0, len(line)):
            if index and i <= index:
                continue

            segment = line[i:i+max_length]

            # Iterating through the data in NUMBERS to find a match
            for num in NUMBERS:
                if segment.startswith(num[0]):
                    # Adding the number in the line, before the spelled out number
                    line = line[:i] + num[1] + line[i:]
                    # Increasing index by 1
                    index = i + 1
                    break

        # Iterating through every character in the line
        for char in line:
            # If the character is a number us added to the 'found_numbers' list
            if char.isnumeric():
                found_numbers.append(char)

        # The first and last values in the 'found_numbers'
        # are used to create the 'calibration_value'
        calibration_value = found_numbers[0] + found_numbers[-1]

        # The 'calibration_value' is added to the 'calibration_values_sum'
        calibration_values_sum += int(calibration_value)

    # The 'calibration_values_sum' is printed to show the result
    print(calibration_values_sum)
