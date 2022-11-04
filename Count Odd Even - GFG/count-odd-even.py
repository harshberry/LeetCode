#User function Template for python3

class Solution:
	def countOddEven(self, arr, n):
	    cd=0
	    ce=0
		for i in range(0,n):
		    if arr[i]%2==0:
		        ce+=1
        print(str(n-ce),'',str(ce))
		    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        arr = list(map(int, input().strip().split()))
    	obj = Solution()
    	obj.countOddEven(arr, n);
# } Driver Code Ends