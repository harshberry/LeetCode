#User function Template for python3


def find(arr,n,x):
    pos =[]
    for i in range(0,n):
        if arr[i] ==x:
            pos.append(i)
    if x not in arr:
        pos.append(-1)
        pos.append(-1)
    return pos[0],pos[-1]



#{ 
 # Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ans=find(arr,n,x)
    print(*ans)
# } Driver Code Ends