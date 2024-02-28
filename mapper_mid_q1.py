#!/usr/bin/env python3
import sys
import uuid

# Read each line and pass it to the reducer
for line in sys.stdin:
    # Strip whitespace from the beginning and end of the line
    line = line.strip()

    # Skip empty lines, this will avoid empty lines to fill output sample size
    if not line:
        continue

    # UUID ensures each key is unique, even across different executions of the map task or across different data sets
    unique_key = uuid.uuid4()
    print(f'{unique_key}\t{line}')
