import sys
sys.stdin = open('test.txt', 'r')

n, x = map(int, input().split())
tours = {}
for _ in range(n):
    l, r, cost = map(int, input().split())
    duration = r - l + 1
    if duration < x:
        if duration not in tours:
            tours[duration] = [(l, r, cost)]
        else:
            tours[duration].append((l, r, cost))



# for duration in tours.keys():
#     tours[duration].sort(key=lambda x: x[2])
#
# answer = 2 * 10 ** 9 + 1
# for duration, fst_tours in tours.items():
#     if x - duration in tours:
#         for fst in fst_tours:
#             if fst[2] < answer:
#                 for snd in tours[x - duration]:
#                     if fst[2] + snd[2] >= answer:
#                         break
#                     if fst[1] < snd[0] or snd[1] < fst[0]:
#                         answer = min(answer, fst[2] + snd[2])
#             else:
#                 break
#
# if answer == 2 * 10 ** 9 + 1:
#     print(-1)
# else:
#     print(answer)
