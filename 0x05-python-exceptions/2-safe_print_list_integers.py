#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                count += 1
                for x in range(count):
                    print("", end="")
        except (IndexError):
            print("", end="")
        print()
        return count
