import re

f = open("input", "r")

coords = set()
instructions = []

for line in f.readlines():
    if re.match("[0-9]+\,[0-9]+", line):
        coord = tuple(map(int, line.strip().split(",")))
        coords.add(coord)
    if re.match("fold along .*", line):
        print("instruction")
        print(line)
        instruction = tuple(line.strip().split()[2].split("="))
        instructions.append((instruction[0], int(instruction[1])))

print(coords)
print(instructions)

fold = instructions[0]
new_cords = set()
for coord in coords:
    x, y = coord
    mag = fold[1]
    if fold[0] == "x":
        if x > mag:
            distance = x - mag
            x = mag - distance
    if fold[0] == "y":
        if y > mag:
            distance = y - mag
            y = mag - distance
    new_cords.add((x,y))
print(len(new_cords))
