#User function Template for python3

class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def mergeArrays(self,a,b,n,m):
        a=set(a)
        b=set(b)
        c=list(a|b)
        d=sorted(c)
        return d
      
        # code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Contributed by : Nagendra Jha
# Modified by : Sagar Gupta


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,m = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))
        b = list(map(int,input().strip().split()))
        ob=Solution()
        li = ob.mergeArrays(a,b,n,m)
        for val in li:
            print(val, end = ' ')
        print()
# } Driver Code Ends