import sys

sys.stdin = open('test.txt', 'r')

good = set(input())
bad = set(chr(i) for i in range(97, 97 + 26)) - good

pattern = input()
star_idx = pattern.find('*')


def comparison(pattern, string):
    global good

    for i in range(len(pattern)):
        if pattern[i] != '?':
            if string[i] != pattern[i]:
                return False
        else:
            if string[i] not in good:
                return False

    return True


for _ in range(int(input())):
    s = input()
    if star_idx == -1:
        if len(s) != len(pattern):
            print('NO')
        elif comparison(pattern, s):
            print('YES')
        else:
            print('NO')
    else:
        if len(pattern) - 1 > len(s):
            print('NO')
        elif comparison(pattern[:star_idx], s[:star_idx]) and \
                comparison(pattern[:star_idx:-1], s[::-1]):
            if set(s[star_idx:len(s) - (len(pattern) - star_idx - 1)]) - bad:
                print('NO')
            else:
                print('YES')
        else:
            print('NO')
