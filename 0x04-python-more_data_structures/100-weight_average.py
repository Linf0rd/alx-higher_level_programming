#!/usr.bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    total = sum([score * weight for score, weight in my_list])
    weights = sum([weight for score, weight in my_list])
    return total / weights if weights != 0 else 0
