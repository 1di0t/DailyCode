import sys

N = int(sys.stdin.readline().rstrip())
end_time, meeting = 0,0
for i in range(N):
    start , end = map(int,sys.stdin.readline().rstrip().split(" "))
    if start > end_time:
        end_time = end
        meeting += 1
    else:
        continue
print(meeting)