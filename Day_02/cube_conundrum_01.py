# Variable for storing the sum eligible game ID's
valid_games_sum = 0

# Variable for storing current game ID
game_id = 1

# Opening file with puzzle input
with open('cube_conundrum_input.txt', 'r') as file:
    # Looping through each line
    for line in file:
        eligible_game = True

        # Removing '\n' from the end of each line
        line = line.strip()

        # Splitting the line on multiple strings when ' ' occurs
        line = line.split(' ')

        # Removing "Game" string
        line.pop(0)

        # Removing "Game ID" string
        line.pop(0)

        for i in range(0, len(line), 2):
            if line[i + 1].startswith("r") and int(line[i]) > 12:
                eligible_game = False
                break
            elif line[i + 1].startswith("g") and int(line[i]) > 13:
                eligible_game = False
                break
            elif line[i + 1].startswith("b") and int(line[i]) > 14:
                eligible_game = False
                break

        if eligible_game:
            valid_games_sum += game_id

        game_id += 1

print(valid_games_sum)
