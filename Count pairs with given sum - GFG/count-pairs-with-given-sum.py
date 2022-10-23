#User function Template for python3

class Solution:
    def getPairsCount(self, arr, n, k):
        
        dict = {}
        pairs = 0
        
        for i in arr:
            if k-i in dict:
                pairs+=dict[k-i]
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        return pairs


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends