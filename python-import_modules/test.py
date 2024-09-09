#!/usr/bin/python3
import sys


print("bonjour:",
      sys.argv[0])
print("Number of elements including the name of the program:",
      len(sys.argv))
print("Number of elements excluding the name of the program:",
      (len(sys.argv)-1))
print("Argument List:",
      str(sys.argv))
