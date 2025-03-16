import sys

sides_arr = []

while True:
    sides = list(map(int,sys.stdin.readline().rstrip().split(" ")))
    sides_arr.append(sides)
    if sides == [0,0,0]:
        break
for i in range(len(sides_arr)-1):
    sides = sides_arr[i]
    sides.sort()

    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        print("right")
    else:
        print("wrong")