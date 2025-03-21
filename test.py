import sys

crain = int(sys.stdin.readline().rstrip())
capacity = sorted(list(map(int, sys.stdin.readline().rstrip().split(" "))),reverse=True)
box_count = int(sys.stdin.readline().rstrip())
box_weight = sorted(list(map(int, sys.stdin.readline().rstrip().split(" "))),reverse=True)

if max(capacity) < max(box_weight):
    print(-1)
else:
    result = 0
    while box_weight:
        for i in range(crain):
            for j in range(len(box_weight)):
                if capacity[i] >= box_weight[j]:
                    del box_weight[j]
                    break
        result += 1
    print(result)