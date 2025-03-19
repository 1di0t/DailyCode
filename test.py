import sys

num = int(sys.stdin.readline().rstrip())
str_arr = []
for i in range(num):
    str_arr.append(list(sys.stdin.readline().rstrip().split(" ")))
    str_arr[i][1] = list(str_arr[i][1])


for i in range(num):
    for l in range(len(str_arr[i][1])):
        for r in range(int(str_arr[i][0])):
            print(str_arr[i][1][l], end="")
    print()