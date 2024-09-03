#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    l_num = -1*number % 10
    l_num = -1*l_num
else:
    l_num = number % 10

if l_num > 5:
    print(f"last digit of {number} is {l_num} and is greater than 5")

elif l_num == 0:
    print(f"last digit of {number} is {l_num} and is 0")

else:
    print(f"last digit of {number} is {l_num} and is less than 6 and not 0")
