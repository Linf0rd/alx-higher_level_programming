#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for l in range(x):
            print(my_list[l], end="")
            count += 1
    except IndexError:
        pass
    finally:
        print()
        return count
