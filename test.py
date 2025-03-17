import sys

bottle = list(map(int,sys.stdin.readline().rstrip().split(" ")))

print(sum(bottle)*5)