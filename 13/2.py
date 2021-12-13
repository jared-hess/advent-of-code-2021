import re
import matplotlib.pyplot as plt


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

def do_instruction(instruction, sheet):
    new_cords = set()
    for coord in sheet:
        x, y = coord
        mag = instruction[1]
        if instruction[0] == "x":
            if x > mag:
                distance = x - mag
                x = mag - distance
        if instruction[0] == "y":
            if y > mag:
                distance = y - mag
                y = mag - distance
        new_cords.add((x,y))
    return new_cords


for fold in instructions:
    coords = do_instruction(fold, coords)

print(coords)
plt.scatter(*zip(*coords))
plt.gca().invert_yaxis()
plt.show()