f = open("input", "r")
steps = 100
flashes = 0

def increase_energy(array):
    new_array = []
    for line in array:
        line = [x+1 for x in line]
        new_array.append(line)
    return new_array
# Create Data Array and mask array
data = []
mask = []
for line in f.readlines():
    ints = [int(x) for x in line.strip()]
    data.append(ints)
    mask_line = [False] * len(ints)
    mask.append(mask_line)
print(data)

for step in range(steps):
    data = increase_energy(data)
    flashed = True
    while(flashed):
        flashed = False
        for i, line in enumerate(data):
            for j, item in enumerate(line):
                # If power is over 9 and we havent' recorded it yet
                if item > 9 and not mask[i][j]:
                    flashed = True
                    mask[i][j] = True
                    flashes+=1
                    neighbor_indexes = [(i+1,j), (i-1,j), (i, j+1), (i, j-1), (i+1, j+1), (i-1, j-1), (i+1, j-1), (i-1, j+1)]
                    for neighbor_index in neighbor_indexes:
                        if 0 <= neighbor_index[0] < len(data) and 0 <= neighbor_index[1] < len(line):
                            data[neighbor_index[0]][neighbor_index[1]]+=1
    print(data)
    # Flashes are complete, reset mask and reset flashed to 0
    for i, line in enumerate(mask):
        for j, item in enumerate(line):
            if item:
                data[i][j] = 0
                mask[i][j] = False
print(flashes)





