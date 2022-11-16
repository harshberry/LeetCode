#User function Template for python3

class Solution:
    def lastIndex(self, s):
        if str(1) not in s:

            return -1

        last = 0

        for i in range(len(tuple(s))):

            if s[i] == '1':

                last = i

        return last
                
        
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
    	s = input()
    	ob = Solution()
    	print(ob.lastIndex(s))
    	
    	T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends