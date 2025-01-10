#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    total_sum = sum([x for x in ar])
    return total_sum


if __name__ == '__main__':
    
    ar=[1,3,7,-1,5,9,4,8]
    result = simpleArraySum(ar)
    print(result)

