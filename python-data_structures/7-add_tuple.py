#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        if len(tuple_a) == 1:
            tuple_a = (tuple_a[0], 0)
        else:
            tuple_a = (0, 0)

    if len(tuple_b) < 2:
        if len(tuple_b) == 1:
            tuple_b = (tuple_b[0], 0)
        else:
            tuple_b = (0, 0)

    sum_1 = tuple_a[0] + tuple_b[0]
    sum_2 = tuple_a[1] + tuple_b[1]

    result = (sum_1, sum_2)
    return (result)
