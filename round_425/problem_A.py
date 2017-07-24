import sys
sys.stdin = open('test.txt', 'r')

n, k = map(int, input().split())

a = n % (2 * k)

if a >= k:
    print('YES')
else:
    print('NO')
