
with open('wait_for_it.txt', 'r') as file:
    time = file.readline().strip().split()
    time.pop(0)
    distance = file.readline().strip().split()
    distance.pop(0)

error_margin = 1

for i in range(0, len(time)):
    time_available = int(time[i])
    record_distance = int(distance[i])

    current_time = time_available
    all_distances = []

    for j in range(0, time_available + 1):
        speed = j
        travel_time = time_available - j

        travel_distance = travel_time * speed

        all_distances.append(travel_distance)

    race_error = 0

    for d in all_distances:
        if record_distance < d:
            race_error += 1

    print(race_error)

    error_margin *= race_error

print(error_margin)
