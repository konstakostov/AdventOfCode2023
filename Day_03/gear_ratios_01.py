DIRECTIONS = [
    (-1, 0),    # Up
    (1, 0),     # Down
    (0, -1),    # Left
    (0, 1),     # Right
    (-1, -1),   # Up-Left
    (-1, 1),    # Up-Right
    (1, -1),    # Down-Left
    (1, 1),     # Down-Right
]

with open('gear_ratios_input.txt', 'r') as file:
    engine = file.read().split('\n')
    engine = [list(block) for block in engine]

SIZE = len(engine[0])
# print(engine)

valid_number = False
next_col = None

engine_numbers_sum = 0

for row in range(len(engine)):
    next_col = None

    for col in range(len(engine[row])):
        if engine[row][col].isdigit():
            if valid_number:
                continue

        valid_number = False

        if engine[row][col].isdigit():
            first_col = col
            last_col = col

            last_col_found = False
            while not last_col_found and last_col + 1 < SIZE:
                last_col += 1
                current = engine[row][last_col]
                if not current.isdigit():
                    last_col -= 1
                    last_col_found = True
                    break

            for direction in DIRECTIONS:
                first_digit_row = row + direction[0]
                first_digit_col = first_col + direction[1]

                last_digit_row = row + direction[0]
                last_digit_col = last_col + direction[1]

                if 0 <= first_digit_row < SIZE and 0 <= first_digit_col < SIZE:
                    current_block = engine[first_digit_row][first_digit_col]

                    if current_block != '.' and not current_block.isnumeric():
                        valid_number = True
                        break

                if 0 <= last_digit_row < SIZE and 0 <= last_digit_col < SIZE:
                    current_block = engine[last_digit_row][last_digit_col]

                    if current_block != '.' and not current_block.isnumeric():
                        valid_number = True
                        break

            if valid_number:
                valid_num = ''
                for i in range(first_col, last_col + 1):
                    valid_num += engine[row][i]

                engine_numbers_sum += int(valid_num)

                next_col = last_col

print(engine_numbers_sum)

