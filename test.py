import sys

def is_same_stack(stack1, stack2, stack2_index):
    if stack1[-1] == stack2[stack2_index]:
        return True



number = int(sys.stdin.readline().rstrip())
input_stack, output_stack, answer_list = [], [], []

for n in range(number):
    answer_list.append(int(sys.stdin.readline().rstrip()))
minus = False
y=0
try:
    for x in range(1,number+1):
        input_stack.append(x)
        output_stack.append('+')
        if is_same_stack(input_stack, answer_list, y):
            minus = True
        while minus:
            if len(input_stack) == 0:
                break
            if input_stack[-1] > answer_list[y]:
                raise Exception
            if is_same_stack(input_stack, answer_list, y):
                input_stack.pop()
                output_stack.append('-')
                y+=1
            else:
                minus = False
                break
    for z in output_stack:
        print(z)
except:
        print('NO')
    

