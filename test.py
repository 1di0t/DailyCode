import sys

N,r,c = map(int,sys.stdin.readline().rstrip().split(" "))

def z(N,r,c):
    if N == 0:
        return 0
    half = 2**(N-1)
    if r < half and c < half:
        return z(N-1,r,c)
    elif r < half and c >= half:
        return half*half + z(N-1,r,c-half)
    elif r >= half and c < half:
        return 2*half*half + z(N-1,r-half,c)
    else:
        return 3*half*half + z(N-1,r-half,c-half)

print(z(N,r,c))

