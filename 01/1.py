f = open("input", "r")

count = 0
prev = int(f.readline())
for line in f:
    cur = int(line)
    print(cur)
    if cur > prev:
        count+=1
        print("increased")
    prev = cur
print(count)
