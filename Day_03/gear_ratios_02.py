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

gear_ratios_sum = 0

for row in range(len(engine)):
    for col in range(len(engine[row])):
        pass


print(gear_ratios_sum)

