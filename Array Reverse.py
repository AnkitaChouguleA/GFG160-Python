# Python Program to reverse an array by swapping elements

def reverseArray(arr):
    n = len(arr)
    
    # Iterate over the first half and for every index i,
    # swap arr[i] with arr[n - i - 1]
    for i in range(n // 2):
        temp = arr[i]
        arr[i] = arr[n - i - 1]
        arr[n - i - 1] = temp

if __name__ == "__main__":
    arr = [1, 4, 3, 2, 6, 5]

    reverseArray(arr)
  
    for i in range(len(arr)):
        print(arr[i], end=" ")


"""
Step	i	arr[i]	arr[n - i - 1]	    Swap Result
1	    0	1	        5	            [5, 4, 3, 2, 6, 1]
2	    1	4	        6	            [5, 6, 3, 2, 4, 1]
3	    2	3	        2	            [5, 6, 2, 3, 4, 1]

"""
