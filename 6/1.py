DAYS = 80
# input = [3,4,3,1,2]
f = open("input", "r")
input = list(map(int, f.readline().strip().split(",")))
print(input)

for day in range(DAYS):
    for i in range(len(input)):
        if input[i] > 0:
            input[i]-=1
        else:
            input[i]=6
            input.append(8)
    print(f"After day {day}: {len(input)}")

