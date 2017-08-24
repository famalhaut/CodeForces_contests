import os
from time import sleep

text = """import sys
sys.stdin = open('tests/test_{ch}.txt', 'r')


"""

contest_name = 'edu_round_27'
num_problems = 7

if not os.path.exists(contest_name):
    os.makedirs(contest_name)
    os.makedirs(contest_name + '/tests')

for i_ch in range(ord('A'), ord('A') + num_problems):
    ch = chr(i_ch)

    open(contest_name + f'/tests/test_{ch}.txt', 'w').close()

    with open(contest_name + f'/problem_{ch}.py', 'w') as f:
        f.write(text.format(ch=ch))
