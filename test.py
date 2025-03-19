import sys

num = []
answer = 0

for i in range(10):
    num.append(int(sys.stdin.readline().rstrip())%42)

num = sorted(num)
for i in range(9):
    if num[i] != num[i+1]:
        answer += 1
        
print(answer+1)
