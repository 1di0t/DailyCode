import sys

number = int(sys.stdin.readline().rstrip())
factorial = 1
answer = 0
for i in range(1, number+1):
    factorial *= i

list_factorial = list(str(factorial))
for i in range(len(list_factorial)-1, -1, -1):
    if list_factorial[i] == '0':
        answer += 1
    else:
        break
print(answer)

    