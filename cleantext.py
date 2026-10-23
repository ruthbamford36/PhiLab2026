#!/usr/bin/env python3

from pathlib import Path

# Input and output files
input_file = "input.txt"
output_file = "output_clean.txt"

# Read file (replace undecodable bytes if necessary)
with open(input_file, "r", encoding="utf-8", errors="replace") as f:
    text = f.read()

# Keep:
#   ASCII printable characters (32-126)
#   newline (\n), carriage return (\r), tab (\t)
cleaned = "".join(
    c for c in text
    if c in "\n\r\t" or (32 <= ord(c) <= 126)
)

with open(output_file, "w", encoding="ascii") as f:
    f.write(cleaned)

print(f"Cleaned file written to: {output_file}")