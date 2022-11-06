# Return true if str is binary, else false
def isBinary(str):
    for i in str:
        if i == '0' or i == '1':
            continue
        else:
            return 0
    return 1


#{ 
 # Driver Code Starts
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        str = input().strip()
        if isBinary(str):
            print (1)
        else:
            print (0)
# } Driver Code Ends