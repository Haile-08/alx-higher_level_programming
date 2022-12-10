#!/usr/bin/python3
def remove_char_at(str, n):
    sl = ""
    for i in range(0, len(str)):
        if i != n:
            sl = sl + str[i]
        else:
            continue
    return (sl)
