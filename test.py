import sys

str = (list(sys.stdin.readline().rstrip()))
comp_arr = []

for i in range(97, 123):
    comp_arr.append(chr(i))

for i in range(len(comp_arr)):
    if comp_arr[i] in str:
        print(str.index(comp_arr[i]), end=' ')
    else:
        print(-1, end=' ')