# your task is to complete this function
# function should return index to the any valid peak element
class Solution:   
    def peakElement(self,arr, n):
        
        if len(arr) == 1:

            return 0
        #checking specifically for the first and last element of arr.
        l = len(arr)
        x = arr[0]

        if x >= arr[1]:

            return 0
            
        y = arr[l-1]

        if y >= arr[l-2]:

            return l - 1
            i=0
        
        for i in range(1,l-2):
            if arr[i]>=arr[i-1] and arr[i]>=arr[i+1]:
                return i
        return 0


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        index = Solution().peakElement(arr.copy(), n)
        flag = False
        if index<0 or index>=n:
            flag = False
        else:
            if index == 0 and n==1:
                flag = True
            elif index==0 and arr[index]>=arr[index+1]:
                flag = True
            elif index==n-1 and arr[index]>=arr[index-1]:
                flag = True
            elif arr[index-1] <= arr[index] and arr[index] >= arr[index+1]:
                flag = True
            else:
                flag = False

        if flag:
            print(1)
        else:
            print(0)
# Contributed by: Harshit Sidhwa

# } Driver Code Ends