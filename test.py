
string_arr = input().strip().split(" ")
if '' in string_arr:
    print(0)
else:
    print(len(string_arr))