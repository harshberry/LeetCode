#User function Template for python3

class Solution:
    def findIndex (self,a, N, key ):
        
        ans=[]
        for i in range(0,N):
            if a[i]==key:
                ans.append(i)
                break
        else:
            ans.append(-1)
            
        for j in range(N-1,-1,-1):
            if a[j]==key:
                ans.append(j)
                break
        else:
            ans.append(-1)
        return ans
        
        
        
  #code here.

       
#{ 
 # Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    key=int(input())
    ob = Solution()
    ans=ob.findIndex(a, n, key )
    print(*ans)
    
# } Driver Code Ends