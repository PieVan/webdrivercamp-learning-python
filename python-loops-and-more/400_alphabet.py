#!/usr/bin/python3

#function

def ASCII():
    for list in range (66,91):
        if list == ord('q'):
            continue
        else:
            print(chr(list).lower() ,end=" ")


ASCII()
