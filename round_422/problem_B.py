import sys
sys.stdin = open('test.txt', 'r')

n, m = map(int, input().split())
s = input()
t = input()

k = len(s)
positions = set()

for i in range(len(t) - len(s) + 1):
    new_k = 0
    new_positions = set()
    for j in range(len(s)):
        if t[i + j] != s[j]:
            new_k += 1
            new_positions.add(j + 1)
        if new_k > k:
            break
    else:
        k = new_k
        positions = new_positions

print(k)
print(*positions)
