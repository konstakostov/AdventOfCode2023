import sys

seeds_data = []
current_map = []

map_data = None

index = 0

with open('fertilizer.py', "r") as almanac:
    seeds = almanac.readline().strip().split()

    for seed in seeds:
        if seed.isnumeric():
            seeds_data.append([int(seed)])

    first_empty_page = almanac.readline()

    for page in almanac:
        page = page.strip().split()

        if not page:
            for data in seeds_data:
                current = data[-1]

                destination = None

                for item in current_map:
                    destination_start = int(item[0])
                    # destination_end = int(item[0]) + int(item[2])
                    source_start = int(item[1])
                    source_end = int(item[1]) + int(item[2])

                    if source_start <= current < source_end:
                        for i in range(source_start, source_end):
                            if current == i:
                                destination = i - source_start + destination_start

                if not destination:
                    destination = current

                seeds_data[index].append(destination)
                index += 1

            current_map = []
            index = 0
            continue

        if not page[0].isnumeric():
            continue

        current_map.append(page)

for data in seeds_data:
    current = data[-1]

    destination = None

    for item in current_map:
        destination_start = int(item[0])
        # destination_end = int(item[0]) + int(item[2])
        source_start = int(item[1])
        source_end = int(item[1]) + int(item[2])

        if source_start <= current < source_end:
            for i in range(source_start, source_end):
                if current == i:
                    destination = i - source_start + destination_start

    if not destination:
        destination = current

    seeds_data[index].append(destination)
    index += 1

lowest_location = sys.maxsize

for seed in seeds_data:
    location = seed[-1]
    print(f"{seed}:     {location}")

    if location < lowest_location:
        lowest_location = location

print(lowest_location)

