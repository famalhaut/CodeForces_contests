import sys
sys.stdin = open('tests/test_B.txt', 'r')

n = int(input())
m = list(map(int, input().split()))

if sum(m) % 2 == 1:
    print('First')
else:
    for i in m:
        if i % 2 == 1:
            print('First')
            break
    else:
        print('Second')
