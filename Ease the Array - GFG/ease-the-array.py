#User function Template for python3

class Solution:
    def modifyAndRearrangeArr (self, arr,  n) :
        
        for j in range(1,len(arr)):
            if arr[j-1] == arr[j] and arr[j]!=0:
                arr[j-1]=2*arr[j]
                arr[j]=0
                t=arr[j-1]
        
        k=0
        for i in range(0,len(arr)):
           if arr[i] !=0:
               arr[i] , arr[k] = arr[k] , arr[i] 
               k+=1   
            



#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob=Solution()
    ob.modifyAndRearrangeArr(arr, n);
    for i in (arr):
        print(i,end= " ")
    print()




# } Driver Code Ends