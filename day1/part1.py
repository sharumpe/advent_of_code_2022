#!/usr/bin/env python3

class Elf:
  def __init__(self,id):
    self.id = id
    self.calories = 0

input_file = open('day1/input1.txt','r')
input_lines = input_file.readlines()

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
    cur_elf = Elf(cur_elf.id + 1)
  else:
    cur_elf.calories += int(line)

print("Elf {} has the most calories, with {}\n".format(max_cal_elf.id,max_cal_elf.calories))
