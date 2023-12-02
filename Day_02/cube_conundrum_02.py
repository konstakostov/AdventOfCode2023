# Variable for storing the sum eligible game ID's
valid_games_power_sum = 0

# Opening file with puzzle input
with open('cube_conundrum_input.txt', 'r') as file:
    # Looping through each line
    for line in file:
        eligible_game = True

        # Max of values of each cube
        max_red = 1
        max_green = 1
        max_blue = 1

        # Removing '\n' from the end of each line
        line = line.strip()

        # Splitting the line on multiple strings when ' ' occurs
        line = line.split(' ')

        # Removing "Game" string
        line.pop(0)

        # Removing "Game ID" string
        line.pop(0)

        for i in range(0, len(line), 2):
            if line[i + 1].startswith("r"):
                if int(line[i]) > max_red:
                    max_red = int(line[i])

            elif line[i + 1].startswith("g"):
                if int(line[i]) > max_green:
                    max_green = int(line[i])

            elif line[i + 1].startswith("b"):
                if int(line[i]) > max_blue:
                    max_blue = int(line[i])

        power_cubes = max_red * max_green * max_blue

        valid_games_power_sum += power_cubes

print(valid_games_power_sum)
