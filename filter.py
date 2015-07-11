#!/usr/bin/python
# fader filter for prose
# think of it as simple procedurally generated horror fiction

from sys import argv
import random

# Read file specified in console argument
# Default to the book of Exodus
if len(argv) > 1:
  filename = argv[-1]
else:
  filename = 'exodus.txt'

with open(filename) as file:
  file_str = file.read()
  outstr = ''
  for i, char in enumerate(file_str):
    freq = float(i) / len(file_str)
    # We skip newliney stuff
    if random.random() < freq and char not in ('\n', '\f', '\r'):
      outstr = outstr + random.choice('gatc')
    else:
      outstr = outstr + file_str[i]

  # print(outstr)

  with open('output.txt', 'w') as outfile:
    outfile.write(outstr)
    print('output written to output.txt')

