import sys


participants = int(sys.stdin.readline().rstrip())
sizes = list(map(int,sys.stdin.readline().rstrip().split(" ")))
bundle_T, bundle_P = map(int,sys.stdin.readline().rstrip().split(" "))
t_order = 0

for i in range(len(sizes)):
    if sizes[i] == 0:
        continue
    elif sizes[i] <= bundle_T:
        t_order += 1
    else:
        t_order += sizes[i]//bundle_T
        if sizes[i]%bundle_T != 0:
            t_order += 1


print(t_order)
print(f"{participants//bundle_P} {participants%bundle_P}")