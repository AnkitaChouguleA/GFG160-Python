# Python Code to left rotate an array using Reversal Algorithm

# Function to rotate an array by d elements to the left
def rotateArr(arr, d):
    n = len(arr)

    # Handle the case where d > size of array
    d %= n

    # Reverse the first d elements
    reverse(arr, 0, d - 1)

    # Reverse the remaining n-d elements
    reverse(arr, d, n - 1)

    # Reverse the entire array
    reverse(arr, 0, n - 1)

# Function to reverse a portion of the array
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    d = 2
    
    rotateArr(arr, d)
  
    for i in range(len(arr)):
        print(arr[i], end=" ")


"""
Step	                      Operation Performed	            Array State
Initial Array	              Given input	                    [1, 2, 3, 4, 5, 6]
Reverse First 𝑑    	        Reverse [1, 2]	                [2, 1, 3, 4, 5, 6]
Reverse Remaining	          Reverse [3, 4, 5, 6]	          [2, 1, 6, 5, 4, 3]
Reverse Entire Array	      Reverse [2, 1, 6, 5, 4, 3]	    [3, 4, 5, 6, 1, 2]
"""
