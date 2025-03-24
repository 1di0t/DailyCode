import sys

N = int(sys.stdin.readline().rstrip())
end_time, meeting , meeting_arr= 0,0,[]
for i in range(N):
    start , end = map(int,sys.stdin.readline().rstrip().split(" "))
    meeting_arr.append([start,end])
meeting_arr = sorted(meeting_arr,key=lambda x:(x[1],x[0]))
for i in meeting_arr:
    if i[0] >= end_time:
        meeting += 1
        end_time = i[1]
    
print(meeting)