import sys


participants = int(sys.stdin.readline().rstrip())
sizes = list(map(int,sys.stdin.readline().rstrip().split(" ")))
bundles = list(map(int,sys.stdin.readline().rstrip().split(" ")))
t_order = 0
pen_order = []


for i in range(len(sizes)):
    if sizes[i] == 0:
        t_order += 0
    if sizes[i] <= bundles[0]:
        t_order += 1
    else:
        t_order += sizes[i] // bundles[0] + 1

pen_order.append(participants//bundles[1])
pen_order.append(participants%bundles[1])

print(t_order)
print(" ".join(map(str,pen_order)))