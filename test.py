import sys

number = list(map(int,sys.stdin.readline().rstrip().split(" ")))
cards = list(map(int,sys.stdin.readline().rstrip().split(" ")))
buffer,answer=[],[]
for i in range(number[0]):
    for j in range(i+1,number[0]):
        for k in range(j+1,number[0]):
            sum= cards[i]+cards[j]+cards[k]
            buffer.append(sum)

for i in range(len(buffer)):
    if number[1] < buffer[i]:
        continue
    else:
        answer.append(buffer[i])

print(max(answer))