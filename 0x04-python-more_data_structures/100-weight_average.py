#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    length = len(my_list)
    new_list = [n * m for n, m in my_list]
    total1 = float(sum(new_list))
    total2 = 0.0
    i = 0
    while i < length:
        total2 += my_list[i][1]
        i += 1

    return float(total1 / total2)
