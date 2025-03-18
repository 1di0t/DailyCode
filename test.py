num_arr = []
answer = 1
for i in range(3):
    num_arr.append(int(input()))

for i in range(len(num_arr)):
    answer *= num_arr[i]

for i in range(10):
    print(str(answer).count(str(i)))