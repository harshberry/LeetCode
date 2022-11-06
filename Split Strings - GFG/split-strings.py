#User function Template for python3

class Solution:
    def splitString(ob, S):
        n=''
        c=''
        s=''
        for i in S:
            if i.isalpha():
                c+=i
            elif i.isdigit():
                n+=i
            else:
                s+=i
        return c,n,s
       


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        S = input()
        ob = Solution()
        ans = ob.splitString(S)
        for i in ans:
            if(i==""):
                print(-1)
            else:
                print(i)


# } Driver Code Ends