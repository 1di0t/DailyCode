import sys

id_arr = []
no = []
for i in range(28):
    id_arr.append(int(sys.stdin.readline().rstrip()))

id_arr.sort()
id,comp_id = 0,1
while comp_id < 31:
    if id == 28:
        no.append(comp_id)
        break
    elif comp_id == id_arr[id]:
        id+=1
    else:
        no.append(comp_id)
    comp_id+=1
    

print(f"{min(no)}\n{max(no)}")