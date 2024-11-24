#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        #Your code here
        n = len(arr)
        d = d%n # Handle cases where d > n
        
        # Call the reverse function
        self.reverse(arr, 0, d-1)
        self.reverse(arr, d, n-1)
        self.reverse(arr, 0, n-1)
        
    # Function to reverse a segment of the array    
    def reverse(self, arr, s, e):
        while s < e:
            arr[s],arr[e] = arr[e],arr[s]
            s = s+1
            e = e-1
            
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())

    while (T > 0):
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ob.rotateArr(A, D)

        for i in A:
            print(i, end=" ")

        print()

        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends


"""
Step	                      Operation Performed	            Array State
Initial Array	              Given input	                    [1, 2, 3, 4, 5, 6]
Reverse First 𝑑    	        Reverse [1, 2]	                [2, 1, 3, 4, 5, 6]
Reverse Remaining	          Reverse [3, 4, 5, 6]	          [2, 1, 6, 5, 4, 3]
Reverse Entire Array	      Reverse [2, 1, 6, 5, 4, 3]	    [3, 4, 5, 6, 1, 2]
"""
