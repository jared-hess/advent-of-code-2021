f = open("input", "r")

def shifting(bitlist):
     out = 0
     for bit in bitlist:
         out = (out << 1) | bit
     return out

def find_most_common(input, position):
    tracker = 0
    for line in input:
        val = line[position]
        if val:
            tracker+=1
        else:
            tracker-=1
    if tracker >= 0:
        return 1
    else:
        return 0
            
def find_least_common(input, position):
    tracker = 0
    for line in input:
        val = line[position]
        if val:
            tracker+=1
        else:
            tracker-=1
    if tracker >= 0:
        return 0
    else:
        return 1

def get_o2_rating(data):
    o2_data = data
    for i in range(12):
        common = find_most_common(o2_data, i)
        o2_data = [x for x in o2_data if x[i] == common]
    return shifting(o2_data[0])

def get_co2_rating(data):
    co2_data = data
    for i in range(12):
        least_common = find_least_common(co2_data, i)
        co2_data = [x for x in co2_data if x[i] == least_common]
        if len(co2_data) == 1:
            return shifting(co2_data[0])
    return shifting(co2_data[0])


data = []
for line in f:
    data_line = [0,0,0,0,0,0,0,0,0,0,0,0]
    for idx, val in enumerate(line.strip()):
        data_line[idx] = int(val)
    data = data + [data_line]

o2 = get_o2_rating(data)
co2 = get_co2_rating(data)
print(f"o2: {o2}, co2: {co2}")
print(o2 * co2)