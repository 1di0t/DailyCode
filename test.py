import sys

def remove_duplicates(input_list):
    result = []
    for item in input_list:
        if item not in result:
            result.append(item)
    return result

num = int(sys.stdin.readline().rstrip())
str_arr = []

for i in range(num):
    buff = sys.stdin.readline().rstrip()
    str_arr.append([len(buff),buff])

str_arr = remove_duplicates(str_arr)
str_arr.sort()

for i in range(len(str_arr)):
    print(str_arr[i][1])