import sys
import array

repeat = int(sys.stdin.readline().rstrip())
S = [20]
def add(num):
    if num not in S:
        S.append(num)
def remove(num):
    if num in S:
        S.remove(num)
def check(num):
    if num in S:
        print(1)
    else:
        print(0)
def toggle(num):
    if num in S:
        S.remove(num)
    else:
        S.append(num)
def all():
    S.clear()
    for i in range(1, 21):
        S.append(i)
def empty():
    S.clear()

for i in range(repeat):
    command = sys.stdin.readline().rstrip().split(" ")
    case = command[0]
    if case == "add":
        add(int(command[1]))
    elif case == "remove":
        remove(int(command[1]))
    elif case == "check":
        check(int(command[1]))
    elif case == "toggle":
        toggle(int(command[1]))
    elif case == "all":
        all()
    elif case == "empty":
        empty()