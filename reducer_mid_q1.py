#!/usr/bin/env python3
import sys
import random

k = int(sys.argv[1])  # The number of samples to collect

reservoir = []  # Initialize an empty reservoir list
count = 0       # Track the total number of lines processed

# Process each line emitted by the mapper
for line in sys.stdin:
    uuid, value = line.strip().split('\t', 1)
    # If the reservoir isn't full, append the line 
    if len(reservoir) < k:
        reservoir.append(value)
    else:
        # As count increases, the probability of replacing an existing item decreases
        p = random.randint(1, count+1) 
        if p < k:
            reservoir[p-1] = value  # Since lists in Python are 0-indexed we want to replace between 0 to count
    count += 1

# Output the final reservoir samples
for r in reservoir:
    print(r)


