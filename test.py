import sys


num_NM = list(map(int,sys.stdin.readline().rstrip().split(" ")))

basket = [0] * num_NM[0]

for i in range(num_NM[1]):
    input_num = list(map(int,sys.stdin.readline().rstrip().split(" ")))
    for j in range(input_num[0], input_num[1]+1):
        if j != 0:
            j -= 1
        basket[j] = input_num[2]

print(" ".join(map(str,basket)))