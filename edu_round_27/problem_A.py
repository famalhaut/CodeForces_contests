import sys
sys.stdin = open('tests/test_A.txt', 'r')

n = int(input())
rs = sorted(map(int, input().split()))

if rs[n-1] != rs[n]:
    print('YES')
else:
    print('NO')
