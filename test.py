import sys

chess = list(map(int,sys.stdin.readline().rstrip().split(" ")))
chess_gudie = [1,1,2,2,2,8]

for i in range(len(chess)):
    chess_gudie[i] = chess_gudie[i] - chess[i]

print(" ".join(map(str,chess_gudie)))