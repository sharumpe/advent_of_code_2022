#!/usr/bin/env python3

_name = {
  0: 'Scissors',
  1: 'Rock',
  2: 'Paper',
  3: 'Scissors'
}
_map = {
  'A': 1,
  'B': 2,
  'C': 0,
  'X': 1,
  'Y': 2,
  'Z': 3
}

def get_outcome(a,b):
  if a == (b-1):
    # B wins!
    return 6 + b
  
  if _name[a] == _name[b]:
    # It's a draw!
    return 3 + b
  
  # It's a loss but you still get points for your shape
  return b
  
# get the input lines
input_file = open('day2/input1.txt','r')
input_lines = input_file.readlines()

final_score = 0
for line in input_lines:
  parts = line.split()
  a = _map[parts[0]]
  b = _map[parts[1]]
  outcome = get_outcome(a,b)
  final_score += outcome
  print(f'{outcome}: {_name[a]} and {_name[b]}')

print(final_score)