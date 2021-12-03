f = open("input", "r")

depth = 0
horiz = 0

for line in f:
    words = line.split()
    direction = words[0]
    magnitude = int(words[1])
    if direction == "up":
        depth-=magnitude
    if direction == "down":
        depth+=magnitude
    if direction == "forward":
        horiz+=magnitude

print(f"Depth: {depth}, Horizontal: {horiz}")
print(f"Result: {depth * horiz}")

    