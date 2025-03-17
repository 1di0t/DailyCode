import sys

ids = list(map(int,sys.stdin.readline().rstrip().split(" ")))
verify = 0

for i in range(len(ids)):
    verify += ids[i] ** 2

print(verify % 10)
