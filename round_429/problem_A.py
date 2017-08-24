import sys
sys.stdin = open('tests/test_A.txt', 'r')

from collections import Counter

n, k = map(int, input().split())
colors = input()

d = Counter(colors)

for color, i in d.items():
    if i > k:
        print('NO')
        break
else:
    print('YES')
