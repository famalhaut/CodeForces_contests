import sys
sys.stdin = open('test.txt', 'r')

good = set(input())

bad = set()
for i in range(97, 97 + 26):
    bad.add(chr(i))
bad = bad - good

pattern = input()

for _ in range(int(input())):
    st = input()
    flag = False

    if len(pattern) - int('*' in pattern) > len(st):
        print('NO')
    else:

        for i, ch in enumerate(pattern):
            if ch not in {'?', '*'}:
                if ch != st[i]:
                    print('NO')
                    break
            elif ch == '?':
                if st[i] not in good:
                    print('NO')
                    break
            elif ch == '*':
                flag = True
                break
        else:
            print('YES')

        if flag:
            for j, ch in enumerate(pattern[::-1], start=1):
                if ch not in {'?', '*'}:
                    if ch != st[-j]:
                        print('NO')
                        break
                elif ch == '?':
                    if st[-j] not in good:
                        print('NO')
                        break
                elif ch == '*':

                    if (i - 1) + j > len(st):
                        print('NO')
                        break
                    else:
                        bad_chs = set(st[i:-(j - 1) + len(st)])
                        if bad_chs - bad:
                            print('NO')
                            break
                        else:
                            print('YES')
                            break
