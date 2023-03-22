import math
import os
import random
import re
import sys
import bisect


def runningMedian(arr):
    l = len(arr)
    if l % 2 == 0:
        x = int(l / 2)
        return (arr[x] + arr[x - 1]) / 2
    else:
        x = int(l / 2)
        return arr[x]

if __name__ == '__main__':
    n = int(input().strip())
    a = []
    for i in range(n):
        a_item = int(input().strip())
        for i in range(len(a) - 1):
            if a[i] < a_item < a[i + 1]:
                a.insert(i + 1, a_item)
        print(float(runningMedian(a)))
