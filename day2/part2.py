#!/usr/bin/env python3

_name = {
  0: 'Scissors',
  1: 'Rock',
  2: 'Paper',
  3: 'Scissors',
  4: 'Rock'
}
_map = {
  'A': 1,
  'B': 2,
  'C': 3,
}

def get_outcome(a,b):
  if b == 'X':
    # Lose
    return 0 + (a-1,3)[a-1==0]
  if b == 'Y':
    # Draw
    return 3 + a
  if b == 'Z':
    # Win!
    return 6 + (a+1,1)[a+1>3]

# get the input lines
input_file = open('day2/input1.txt','r')
input_lines = input_file.readlines()

final_score = 0
for line in input_lines:
  parts = line.split()
  a = _map[parts[0]]
  b = parts[1]
  outcome = get_outcome(a,b)
  final_score += outcome
  print(f'{outcome}: {_name[a]} and {b}')

print(final_score)
