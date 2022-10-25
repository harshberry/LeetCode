#User function Template for python3

class Solution:
    #Function to find triplets with zero sum.    
    def findTriplets(self, arr, n):
        dct = {} # create a frequency dictionary

        for m in arr:

            dct[m] = dct.get(m, 0) + 1

        for i in range(n):

            for j in range(i+1, n):

                z = -(arr[i]+arr[j])

                if z==arr[i] or z==arr[j]: #if the sum is one from the pair

                    if dct.get(z, 0)>1:

                        return True

                else: 

                    if z in dct:

                        return True

        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().strip().split()))
        if(Solution().findTriplets(a,n)):
            print(1)
        else:
            print(0)
# } Driver Code Ends