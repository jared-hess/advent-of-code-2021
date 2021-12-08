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

    digit_to_displayed_segments = {
        0: frozenset(),
        1: frozenset(),
        2: frozenset(),
        3: frozenset(),
        4: frozenset(), 
        5: frozenset(),
        6: frozenset(),
        7: frozenset(),
        8: frozenset(),
        9: frozenset()
    }


    for reading in readings:
        num_segments = len(reading)
        if num_segments in unique_mappings.keys():
           val = unique_mappings[num_segments] 
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
    
    # If a digit has bottom_left, it is a 0, 2, 6, or 8. And we know 8
    for reading in reading_set:
        if segment_mapping["bottom_left"] in reading:
            if reading is not digit_to_displayed_segments[8]:
                if len(reading) == 5: # It's a 2
                    digit_to_displayed_segments[2] = reading
                if len(reading) == 6: # It's a 0 or 6
                    if digit_to_displayed_segments[1].issubset(reading):
                        # If it contains the same segments as digit 1, it's a 0
                        digit_to_displayed_segments[0] = reading
                    else:
                        # Otherwise it's a 6
                        digit_to_displayed_segments[6] = reading
    
    # The only ones we have left are 3, 5, 9. 9 is the only one with 6 segments
    for reading in reading_set - set(digit_to_displayed_segments.values()):
        if len(reading) == 6:
            digit_to_displayed_segments[9] = reading

    # Get 3
    for reading in reading_set - set(digit_to_displayed_segments.values()):
        if digit_to_displayed_segments[1].issubset(reading):
            digit_to_displayed_segments[3] = reading

    # 5 is the only one left
    for reading in reading_set - set(digit_to_displayed_segments.values()):
        digit_to_displayed_segments[5] = reading

    # Now get the outputs
    segments_to_digits = {v: k for k, v in digit_to_displayed_segments.items()}
    output_num_str = [str(segments_to_digits[x]) for x in outputs]
    output_num = int("".join(output_num_str))
    counter+=output_num

print(counter)
