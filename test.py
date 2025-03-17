import sys

integer = list(map(int, sys.stdin.readline().rstrip().split(" ")))

if integer[0] + integer[1] == integer[2]:
    print("correct!")
else:
    print("wrong!")