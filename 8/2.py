from os import read


f = open("input", "r")

def get_single_value(input_set):
    return next(iter(input_set))

all_segments = ["a", "b", "c", "d", "e", "f", "g"]
# Maps number of segments to int display value for unique numbers
unique_mappings = {
    2: 1,
    4: 4,
    3: 7,
    7: 8 
}


counter = 0
values = 2,4,3,7 
for line in f.readlines():
    readings_raw, display_raw = line.split(" | ")
    readings = list(map(frozenset, readings_raw.strip().split()))
    outputs = list(map(frozenset, display_raw.strip().split()))
    print(readings)

    digit_to_displayed_segments = {
        0: {},
        1: {},
        2: {},
        4: {}, 
        6: {},
        7: {},
        8: {}
    }


    for reading in readings:
        print(f"Checking reading {reading}")
        num_segments = len(reading)
        if num_segments in unique_mappings.keys():
           val = unique_mappings[num_segments] 
           print(f"{reading} is a {val}")
           digit_to_displayed_segments[val] = reading

    segment_mapping = {
        "top": None,
        "top_left": None,
        "top_right": None,
        "middle": None,
        "bottom_left": None,
        "bottom_right": None,
        "bottom": None
    }

    # Get the top segment
    top = get_single_value((digit_to_displayed_segments[7] - digit_to_displayed_segments[1]))
    segment_mapping["top"] = top

    # Get bottom left segment (uniquely occurs in 4 digits)
    # print(readings)
    reading_set = set(readings)
    for segment in all_segments:
        occurrances = 0
        for reading in reading_set:
            if segment in reading:
                occurrances+=1
        if occurrances == 4:
            segment_mapping["bottom_left"] = segment
    
    # If a digit has bottom_left, it is a 0, 2, 6, or 8. And we know 8, and 0, 2, and 6 all have different numbers of segments
    for reading in reading_set:
        if segment_mapping["bottom_left"] in reading:
            if reading is not digit_to_displayed_segments[8]:
                if len(reading) == 6: # It's a 0
                    digit_to_displayed_segments[0] = reading
                if len(reading) == 5: # It's a 2
                    digit_to_displayed_segments[2] = reading
                if len(reading) == 6: # It's a 6
                    digit_to_displayed_segments[6] = reading
                    
        
    
    print(segment_mapping)