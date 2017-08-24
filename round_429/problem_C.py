import sys
sys.stdin = open('tests/test_C.txt', 'r')

m = int(input())

m_a = list(map(int, input().split()))
m_b = list(map(int, input().split()))

sort_m_a = sorted(m_a, reverse=True)
sort_m_b = sorted(m_b)

d = dict()

for i, num in enumerate(sort_m_b):
    if num not in d:
        d[num] = [i]
    else:
        d[num].append(i)

for num in m_b:
    print(sort_m_a[d[num].pop()], end=' ')
