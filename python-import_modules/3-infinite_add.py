#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    total_sum = 0
    for args in sys.argv[1:]:
        total_sum += int(args)
    print("{}".format(total_sum))
