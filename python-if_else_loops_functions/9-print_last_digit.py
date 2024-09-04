#!/usr/bin/python3
def print_last_digit(number):
    l_num = abs(number) % 10
    print(f"{l_num}", end="")
    return l_num
