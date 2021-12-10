import math


def dist(x1, y1, x2, y2):
    # Distance between two points
    return math.hypot(x2 - x1, y2 - y1)

def is_on_line(xp, yp, x1, y1, x2, y2):
    dist_total = dist(x1, y1, x2, y2)
    dist1 = dist(x1, y1, xp, yp)
    dist2 = dist(x2, y2, xp, yp)
    return math.isclose(dist_total, dist1 + dist2)

f = open("input", "r")

points = []
for item in range(1000):
    temp = [0]*1000
    points.append(temp)

for line_no, line in enumerate(f):
    print(f"Processing line {line_no}")
    p1, p2 = line.strip().split(" -> ")
    x1, y1 = tuple(map(int, p1.split(",")))
    x2, y2 = tuple(map(int, p2.split(",")))
    for i, row in enumerate(points):
        for j, point in enumerate(row):
            if is_on_line(i, j, x1, y1, x2, y2) and (x1 == x2 or y1 == y2):
                points[i][j]+=1
print(points)

counter = 0
for i, row in enumerate(points):
    for j, point in enumerate(row):
        if point > 1:
            counter+=1
print(counter)
