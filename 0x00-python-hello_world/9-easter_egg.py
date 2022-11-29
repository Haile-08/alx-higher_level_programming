#!/usr/bin/python3
fl = open("The_Zen_of_python.txt", "r")
l = fl.read()[:-1]
print(l)
fl.close()
