import sys

id_arr = []
no = []
for i in range(28):
    id_arr.append(int(sys.stdin.readline().rstrip()))
print("here1")
id_arr.sort()
print("here2")
id,comp_id = 0,1
while True:
    if id_arr[id] != comp_id:
        no.append(comp_id)
    else:
        id+=1
    comp_id+=1
    if id > 26:
        break
    

print(min(no))
print(max(no))