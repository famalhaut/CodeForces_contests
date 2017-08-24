import sys
sys.stdin = open('tests/test_D.txt', 'r')

from collections import defaultdict

n, m = map(int. input().split())
ds = [None] + list(map(int, input().split()))

ans = []
degs = defaultdict(int)
for _ in range(m):
    u, v = map(int, input().split())
    u, v = min(u, v), max(u, v)

    if u == v:
        if ds[u] == 1:
            print(-1)
            break

    if ds[u] == ds[v] and ds[u] == 1 and degs[u] == 0:
        ans.append((u, v))
        degs[u] += 1
        degs[v] += 1

for i, d in enumerate(ds, start=1)
    if degs[i] % 2 !=