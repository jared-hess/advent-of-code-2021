from statistics import mean
# data = [16,1,2,0,4,2,7,1,2,14]

f = open("input", "r")
data = list(map(int, f.readline().strip().split(",")))

def calc_fuel_usage(point, crabs):
    movements = [(pow(abs(x - point),2) + abs(x - point))/2 for x in crabs]
    print(movements)
    return sum(movements)

# print(calc_fuel_usage(5, data))

max_crab = max(data)
running_min = 1000000000
for pos in range(max_crab):
    fuel = calc_fuel_usage(pos, data)
    if fuel < running_min:
        running_min = fuel
print(running_min)

