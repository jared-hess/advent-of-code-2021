from os import read


f = open("input", "r")

counter = 0
values = 2,4,3,7 
for line in f.readlines():
    readings_raw, display_raw = line.split(" | ")
    readings = readings_raw.strip().split()
    outputs = display_raw.strip().split()
    print(readings)
    for output in outputs:
        print(f"Checking output {output}")
        if any(len(output) == v for v in values):
            counter+=1
print(counter)