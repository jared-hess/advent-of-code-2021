f = open("input", "r")

def safe_list_get (l, idx, default):
  try:
    return l[idx]
  except IndexError:
    return default

data = []


counter = 0

for line in f.readlines():
    line_ints = [int(x) for x in line.strip()]
    data.append(line_ints)

for i, row in enumerate(data):
    for j, item in enumerate(row):
        try:
            if i > 0:
                up = data[i-1][j]
            else:
                up = None
        except:
            up = None
        try:
            down = data[i+1][j]
        except:
            down = None
        try:
            if j > 0:
                left = data[i][j-1]
            else:
                left = None
        except:
            left = None
        try:
            right = data[i][j+1]
        except:
            right = None
        
        if (up == None or item < up) and (down == None or item < down) and (left == None or item < left) and (right == None or item < right):
            print(f"Low level found: {i},{j}: {item}")
            score = item + 1
            # print(f"Score: {score}")
            counter+=score
            # print(f"counter: {counter}")
print(counter)

