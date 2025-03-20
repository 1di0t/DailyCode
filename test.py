import sys

number = int(sys.stdin.readline().rstrip())
num_arr = list(map(int,sys.stdin.readline().rstrip().split(" ")))


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def count_prime(number,num_arr):
    answer = 0
    for i in range(number):
        if is_prime(num_arr[i]):
            answer += 1

    return answer
print(count_prime(number,num_arr))