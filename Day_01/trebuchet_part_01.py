with open('trebuchet_input.txt', 'r') as f:
    calibration_document = f.read().split('\n')

calibration_values_sum = 0

for data in calibration_document:
    calibration_values = ""
    found_numbers = []

    for char in data:
        if char.isnumeric():
            found_numbers.append(char)

    calibration_values = found_numbers[0] + found_numbers[-1]

    calibration_values_sum += int(calibration_values)

print(calibration_values_sum)
