f = open("input", "r")

data = []

low_points = []
basins = {}
for line in f.readlines():
    line_ints = [int(x) for x in line.strip()]
    data.append(line_ints)

def find_basin(x, y):
    value = data[x][y]
    neighbors = {}
    # print(f"{x}, {y}")
    if x > 0:
        coords = (x-1, y)
        neighbors[coords] = data[coords[0]][coords[1]]
    if x < (len(data) - 1):
        coords = (x+1, y)
        neighbors[coords] = data[coords[0]][coords[1]]
    if y > 0:
        coords = (x, y-1)
        neighbors[coords] = data[coords[0]][coords[1]]
    if y < (len(data[0]) - 1):
        coords = (x, y+1)
        neighbors[coords] = data[coords[0]][coords[1]]
    
    lowest_neighbor = min(neighbors, key=neighbors.get)
    if neighbors[lowest_neighbor] > value:
        return x,y
    else:
        return find_basin( *lowest_neighbor )


for i, row in enumerate(data):
    for j, item in enumerate(row):
        if item < 9:
            basin = find_basin(i, j) 
            # print(basin)
            if basin in basins.keys():
                basins[basin].append((i,j))
            else:
                basins[basin] = [basin]
print(basins)
basin_sizes = [len(x) for x in basins.values()]
basin_sizes.sort(reverse=True)
print(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])

