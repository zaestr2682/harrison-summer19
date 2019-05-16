# Usage: python calculate-vectors.py

import random
import math

print ""
print "##########"
print "Author: Dr. Nathan Harrison"
print "Instructions: Do it."
print "Comments: All angles are in degrees and defined counter-clockwise with respect to the x-axis."
print "##########"

names = ["Vx", "Vy", "magnitude", "theta"]

for j in range(1, 16):
  ri1 = -1 # random index
  ri2 = -1
  while (ri1 == 0 and ri2 == 2) or (ri1 == 1 and ri2 == 2) or (ri1 == 2 and ri2 == 0) or (ri1 == 2 and ri2 == 1) or (ri1 == ri2):
    ri1 = random.randint(0, len(names)-1)
    ri2 = random.randint(0, len(names)-1)
  
  vx = random.uniform(-5.0, 5.0)
  vy = random.uniform(-5.0, 5.0)
  r = math.sqrt(vx*vx + vy*vy)
  th = 180.0*math.atan2(vy, vx)/math.pi
  if th < 0: th = 360.0 + th
  vals = [vx, vy, r, th]
  
  indices = [0, 1, 2, 3]
  indices.remove(ri1)
  indices.remove(ri2)
  
  print ""
  print "###", j, "###"
  print "First draw a picture of the vector!"
  print "Given ", names[ri1], " = ", vals[ri1], " and ", names[ri2], " = ", vals[ri2]
  
  correct = False
  while correct == False:
    ans = float(input("What is " + names[indices[0]] + "? "))
    if (ans > vals[indices[0]]-0.025 and ans < vals[indices[0]]+0.025) or ans == 1234:
      print "good"
      correct = True
    else:
      print "nope"
  
  correct = False
  while correct == False:
    ans = float(input("What is " + names[indices[1]] + "? "))
    if (ans > vals[indices[1]]-0.025 and ans < vals[indices[1]]+0.025) or ans == 1234:
      print "good"
      correct = True
    else:
      print "nope"

print ""
print "Woo-hoo"

