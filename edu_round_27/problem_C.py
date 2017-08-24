# http://codeforces.com/contest/845/problem/C

import sys
sys.stdin = open('tests/test_C.txt', 'r')

n = int(input())

shows = []
for _ in range(n):
    shows.append(tuple(map(int, input().split())))

shows.sort()

end_1 = -1
end_2 = -1
for show in shows:
    if show[0] > end_1:
        end_1 = show[1]
        continue
    if show[0] > end_2:
        end_2 = show[1]
        continue
    else:
        print('NO')
        break
else:
    print('YES')
