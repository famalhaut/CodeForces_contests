import sys
sys.stdin = open('tests/test_E.txt', 'r')

n, m, k = map(int, input().split())

dots = []
for _ in range(k):
    dots.append(tuple(map(int, input().split())))
