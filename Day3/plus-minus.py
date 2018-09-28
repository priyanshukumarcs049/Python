import math
import os
import random
import re
import sys

n = float(raw_input())
lst = [int(x) for x in raw_input().split()]
print format(len([x for x in lst if x > 0])/n, ".6f")
print format(len([x for x in lst if x < 0])/n, ".6f")
print format(len([x for x in lst if x == 0])/n, ".6f")

if __name__ == '__main__':
    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    plusMinus(arr)