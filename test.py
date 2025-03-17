import sys

zero_one = list(map(int, sys.stdin.readline().rstrip().split(" ")))

if zero_one[0] == zero_one[1] != zero_one[2] :
    print("C")
elif zero_one[0] == zero_one[2] != zero_one[1] :
    print("B")
elif zero_one[1] == zero_one[2] != zero_one[0] :
    print("A")
else: 
    print("*")