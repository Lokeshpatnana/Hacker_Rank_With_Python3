""" HackerRank- Python If-Else """

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    if n%2!=0:
        print('Weird')
    elif n%2==0 and n in range(2,5):
        print('Not Weird')
    elif n%2==0 and n in range(6,20):
        print('Weird')
    elif n%2==0 and n>20:
        print('Not Weird')
    else:
        print("Weird")


#example:

# a=int(input())
# if(a%2==0):
#     print("Even Number")
# else:
#     print("odd number")