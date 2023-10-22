#!/usr/bin/python3
import sys

print(sys.argv)

lengh = len(sys.argv)
if len==0:
    print("0 arguments")
else:
    for i in range(1,lengh):
        print(f"{i}: {sys.argv[i]}")
        i += 1
