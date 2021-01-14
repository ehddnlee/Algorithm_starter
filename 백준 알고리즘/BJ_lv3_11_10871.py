import sys
N, X = map(int, input().split())
A_list = list(map(int, sys.stdin.readline().split()))
for i in range(N):
    if A_list[i] < X:
        print(A_list[i], end = " ")
