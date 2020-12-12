#!/usr/bin/env python3

# Global array for hole values 
hole = [ 1, 0, 0, 0, 1, 0, 1, 0, 2, 1 ] 

# Function to return the count of holes in num
def count_holes(num): 
  try:
    int(num)
  except (TypeError, ValueError):
              #catch incorrect input of an integer
    return print ('error')

  else:
    str(num)  # because 'int' object is not subscriptable

              #drop the first '0' in the sequence 'num'
  if num[0] == '0':
    numers = int(num[1:])
  else: numers = int(num)

  holes = 0

  while (numers > 0) : 
              # find last digit in 'num'
    d = numers % 10
              # accumulate holes
    holes = holes + hole[d]
              # remove last digit 
    numers = numers//10

  return print(holes)    # successful exit

if __name__ == "__main__":
    __name__
