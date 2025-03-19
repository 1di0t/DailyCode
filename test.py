import sys

def check_sort(arr):
    if arr == sorted(arr):
        return "ascending"
    elif arr == sorted(arr, reverse=True):
        return "descending"
    else:
        return "mixed"

music = list(map(int,sys.stdin.readline().rstrip().split(" ")))

print(check_sort(music))

        