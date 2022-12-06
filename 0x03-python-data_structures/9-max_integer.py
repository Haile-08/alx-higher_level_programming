#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max_num = 0
        for i in my_list:
            if i > max_num:
                max_num = i
            else:
                continue
        return max_num
