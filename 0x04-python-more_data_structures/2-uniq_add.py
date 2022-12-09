#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list:
        unique_num = set(my_list)
        s = 0
        for i in unique_num:
            s = s + i
        return s
