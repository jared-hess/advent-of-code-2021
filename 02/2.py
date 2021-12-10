f = open("input", "r")

depth = 0
horiz = 0
aim = 0

for line in f:
    words = line.split()
    direction = words[0]
    magnitude = int(words[1])
    if direction == "up":
        aim-=magnitude
    if direction == "down":
        aim+=magnitude
    if direction == "forward":
        horiz+=magnitude
        depth+=magnitude*aim

print(f"Depth: {depth}, Horizontal: {horiz}, Aim: {aim}")
print(f"Result: {depth * horiz}")

    