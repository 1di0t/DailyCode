import sys

pay, money1, money2 = map(int, sys.stdin.readline().rstrip().split(" "))
answer, pay_money, n, m, buff = 0,0,0,0,None

def compareChange(pay, total):
    return True if pay >= total else False

while compareChange(pay, pay_money):
    while compareChange(pay, pay_money):
        pay_money = money1 * n + money2 * m
        if pay_money < pay:
            m+=1
            continue
        elif pay_money == pay:
            answer = pay_money
            break
        else:
            if buff == None: buff = pay_money
            elif buff>pay_money: buff = pay_money
            answer = buff
    m=0
    n+=1
    pay_money = money1 * n + money2 * m
    

print(answer)