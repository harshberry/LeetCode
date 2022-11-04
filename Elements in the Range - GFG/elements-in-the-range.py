class Solution:
    def check_elements(self, arr, n, A, B):
        arr=set(arr)
        arr=list(arr)
        arr=sorted(arr)
        c=0
        for i in range(len(arr)):
            if(arr[i]>=A and arr[i]<=B):
                c+=1
        if(c==B-A+1):
            return(True)
        else:
            return(False)
                
        


#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        l = list(map(int, input().split()))
        n=l[0]
        k=l[1]
        y=l[2]
        a = list(map(int,input().split()))
        ob = Solution()
        ans=ob.check_elements(a,n,k,y)
        if(ans):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends