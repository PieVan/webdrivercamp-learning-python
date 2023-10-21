#!/usr/bin/python3
import random
random_num = random.randint(-1000, 1000)

last_digit = abs(random_num) % 10

#status even/odd

if random_num % 2 == 0:
    status_even_odd = "even"
else:
    status_even_odd = "odd"

def printSpecialFormat():
    if random_num == 0:
        print(f"{random_num} - the last digit {last_digit} is zero")
    else:
        print(f"{random_num} - the last digit {last_digit} is {status_even_odd}")
printSpecialFormat()
