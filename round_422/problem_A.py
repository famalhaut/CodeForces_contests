import math

# import sys
# sys.stdin = open('test.txt', 'r')

a, b = map(int, input().split())

print(math.factorial(min(a, b)))
