#!/usr/bin/python3
for i in range(100):
    if i < 99:
        print(end="{:02d}, ".format(i))
    else:
        print("{}".format(i))
