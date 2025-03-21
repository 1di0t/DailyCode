import sys

number = int(sys.stdin.readline().rstrip())
num_arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))
other_side = [[0,5],[1,4],[2,3]]
n1, answer = 0, 0
n2, n3 = [], []

if number == 0:
    answer = 0
elif number == 1:
    answer = sum(num_arr)-max(num_arr)
else:
    #면이 1개일때 최소값
    n1 = min(num_arr)

    #면이 2개일때 최소값
    for x in range(len(num_arr)):
        for y in range(x+1, len(num_arr)):
            if [x,y] in other_side:
                continue
            else:
                n2.append(num_arr[x] + num_arr[y])

    #면이 3개일때 최소값
    for x in range(0,6,5):#A,F 일 경우
        for y in range(1,5,3):#B,E 일 경우
            for z in range(2,4):#C,D 일 경우
                n3.append(num_arr[x] + num_arr[y]+ num_arr[z])
    
    n3_count = 4
    n2_count = 8*number-12
    n1_count = 5*(number**2)-(16*number)+12

    answer = min(n3)*n3_count + min(n2)*n2_count+n1*n1_count
print(answer)