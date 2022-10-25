#User function Template for python3

def rotate( a, n):
    temp=a[n-1]
    for i in range(len(a)-1,0,-1):
        a[i]=a[i-1]
    a[0]=temp
    return a
    
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        rotate(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends