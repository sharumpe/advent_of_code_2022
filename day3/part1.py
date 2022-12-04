#!/usr/bin/env python3

import string
letters = list(string.ascii_letters)

# get the input lines
input_file = open('day3/input1.txt','r')
input_lines = input_file.readlines()

total = 0
for line in input_lines:
  part1 = line[0:int(len(line)/2)]
  part2 = line[int(len(line)/2):]
  for c in part1:
    if c in part2:
      priority = letters.index(c) + 1
      total += priority
      # print(f'{c} index: {priority}')
      break
print(f'total: {total}')