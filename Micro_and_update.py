t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    if min(a)<k:
        print(k-min(a))
    else:
        print(0)
