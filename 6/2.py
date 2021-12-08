DAYS = 256
# input = [3,4,3,1,2]
f = open("input", "r")
input = list(map(int, f.readline().strip().split(",")))

# List of number of fish of a given age
ages = [0] * 9

# Load input
for age in input:
    ages[age]+=1
print(ages)

for day in range(DAYS):
    temp = 0
    for age in reversed(range(len(ages))):
        old_age = ages[age]
        ages[age] = temp
        if age == 0: 
            ages[6]+=old_age
            ages[8]=old_age
            # temp is now dirty but it will get reset to 0 next day
        else:
            temp = old_age

print(sum(ages))

