import sys

number = int(sys.stdin.readline().rstrip())
num_arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))
n1,n2,n3, answer = 0, 0, 0, 0

if number == 0:
    answer = 0
elif number == 1:
    answer = sum(num_arr)-max(num_arr)
else:
    #면이 1개일때 최소값
    n1 = min(num_arr)

    #면이 2개일때 최소값
    n2 = min([num_arr[0]+num_arr[1],num_arr[0]+num_arr[2],num_arr[0]+num_arr[3],num_arr[0]+num_arr[4],
           num_arr[5]+num_arr[1],num_arr[5]+num_arr[2],num_arr[5]+num_arr[3],num_arr[5]+num_arr[4],
           num_arr[1]+num_arr[2],num_arr[1]+num_arr[3],
           num_arr[4]+num_arr[2],num_arr[4]+num_arr[3]])

    #면이 3개일때 최소값
    n3 = min([num_arr[0]+num_arr[1]+num_arr[2],num_arr[0]+num_arr[1]+num_arr[3],num_arr[0]+num_arr[4]+num_arr[2],num_arr[0]+num_arr[4]+num_arr[3],
              num_arr[5]+num_arr[1]+num_arr[2],num_arr[5]+num_arr[1]+num_arr[3],num_arr[5]+num_arr[4]+num_arr[2],num_arr[5]+num_arr[4]+num_arr[3]])
    
    n3_count = 4
    n2_count = 8*number-12
    n1_count = 5*(number**2)-(16*number)+12

    answer = n3*n3_count + n2*n2_count+n1*n1_count
print(answer)
