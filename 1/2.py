f = open("input", "r")

count = 0
window = [int(f.readline()), int(f.readline()), int(f.readline())]
prevsum = window[0] + window[1] + window[2]
print(prevsum)
for line in f:
    cur = int(line)
    window = [cur] + window
    sum = window[0] + window[1] + window[2]
    if sum > prevsum:
        count+=1
        print("increased")
    prevsum = sum
print(count)
