import sys

def check_score(arr):
    score,each = 0,0
    for i in range(len(arr)):
        if arr[i] == 'O':
            each += 1
            score += each
        else:
            each = 0
    return score

num = int(sys.stdin.readline().rstrip())
ans_arr = []

for i in range(num):
    ans_arr.append(list(sys.stdin.readline().rstrip()))

for i in range(num):
    print(check_score(ans_arr[i]))
