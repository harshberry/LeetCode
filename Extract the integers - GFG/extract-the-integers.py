#User function Template for python3

class Solution:

    def extractIntegerWords(self, s):
        ans=[]

        n=''

        for i in s:
            if i.isnumeric()==True:
                n+=i
            elif len(n)>=1:
                ans.append(n)
                n=''
        if len(n)>=1:

            ans.append(n)

                

        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        if solObj.extractIntegerWords(s):
            print(*solObj.extractIntegerWords(s))
        else:
            print("No Integers")

# } Driver Code Ends