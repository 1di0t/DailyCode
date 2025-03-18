test_num = int(input())
case = []*test_num

for i in range(test_num):
    case.append(list(map(int,input().split(" "))))

for i in range(test_num):
    w_num = case[i][2] // case[i][0]
    if case[i][2] % case[i][0] != 0:
        w_num += 1
    h_num = case[i][2] % case[i][0]
    if h_num == 0:
        h_num = case[i][0]
    if w_num < 10:
        w_num = '0'+str(w_num)
    print(str(h_num)+str(w_num))
