with open('wait_for_it.txt.', 'r') as file:
    time_data = file.readline().strip().split()
    time_data.pop(0)
    distance_data = file.readline().strip().split()
    distance_data.pop(0)

time, distance = '', ''

for td in range(len(time_data)):
    time += time_data[td]
    distance += distance_data[td]

time, distance = int(time), int(distance)


ways_to_win = 0

for j in range(0, time + 1):
    speed = j
    travel_time = time - j

    travel_distance = travel_time * speed

    if travel_distance > distance:
        ways_to_win += 1

print(ways_to_win)
