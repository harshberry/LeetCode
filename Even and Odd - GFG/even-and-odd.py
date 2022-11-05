#User function Template for python3

class Solution:
    def reArrange(self, arr, N):
        e=0

        o=1

        while(e<N and o<N):  

            if arr[e]%2!=0 and arr[o]%2!=1:

                arr[o],arr[e]=arr[e],arr[o]

                e=e+2

                o=o+2

            elif arr[e]%2!=0 and arr[o]%2==1:

                o=o+2

            elif arr[o]%2!=1 and arr[e]%2==0:

                e=e+2

            elif arr[e]%2==0 and arr[o]%2==1:

                e=e+2

                o=o+2
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def check(arr, n):
    flag = 1
    c=d=0
    for i in range(n):
        if i%2==0:
            if arr[i]%2:
                flag = 0
                break
            else:
                c+=1
        else:
            if arr[i]%2==0:
                flag = 0
                break
            else:
                d+=1
    if c!=d:
        flag = 0
            
    return flag
        
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        ob.reArrange(arr,N)
        
        print(check(arr,N))

# } Driver Code Ends