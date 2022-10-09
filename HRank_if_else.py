number = int(input())

if 1<=number<=100:
    if number%2 !=0:
        print("Weird")
    elif number%2==0:
        if 2<=number<=5:
            print("Not Weird")
        elif 6<=number<=20:
            print("Weird")
        else:
            print("Not Weird")

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(raw_input().strip())
