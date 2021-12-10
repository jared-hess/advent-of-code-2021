f = open("input", "r")

def shifting(bitlist):
     out = 0
     for bit in bitlist:
         out = (out << 1) | bit
     return out

tracker = [0,0,0,0,0,0,0,0,0,0,0,0]
for line in f:
    print(line)
    for idx, val in enumerate(line.strip()):
        print(f"{idx} {val}")
        if int(val):
            tracker[idx]+=1
        else:
            tracker[idx]-=1
print(tracker)

gamma = [0,0,0,0,0,0,0,0,0,0,0,0]
epsilon = [0,0,0,0,0,0,0,0,0,0,0,0]
for idx, val in enumerate(tracker):
    if val > 0:
        gamma[idx] = 1
        epsilon[idx] = 0
    else:
        gamma[idx] = 0
        epsilon[idx] = 1
print(gamma)
print(epsilon)

print(shifting(gamma)*shifting(epsilon))