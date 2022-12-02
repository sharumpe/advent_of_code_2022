#!/usr/bin/env python3

class Elf:
  def __init__(self,id):
    self.id = id
    self.calories = 0
  def __str__(self):
    return f'{self.id} has {self.calories}'

input_file = open('day1/input1.txt','r')
input_lines = input_file.readlines()

elves = []
cur_elf = Elf(0)
max_cal_elf = cur_elf

for line in input_lines:
  # start adding numbers, storing when we hit a blank line
  if line in ['\n','\r\n']:
    # we're done with this elf's pack

    # is this the biggest? update things if so
    if cur_elf.calories > max_cal_elf.calories:
      max_cal_elf = cur_elf

    # put the previous elf in the list and start on a new one
    elves.append(cur_elf)
    cur_elf = Elf(len(elves))
  else:
    cur_elf.calories += int(line)

# Got our list of elf objects
# Sort and find the top 3
sorted_elves = sorted(elves, key=lambda x: x.calories, reverse=True)[0:3]

top_3_total = 0
for elf in sorted_elves:
  top_3_total += elf.calories
  print(elf)

print(f'top 3 total: {top_3_total}')