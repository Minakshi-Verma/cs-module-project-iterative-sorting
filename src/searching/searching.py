def linear_search(arr, target):
    # Your code here    
    for i in range(0, len(arr)):
        if arr[i]==target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):    
    #if target is in middle
    #if target< arr[middle], it would be in the left
    # else it would be in right
    # middle= len(arr)//2
    low= 0
    high= len(arr)-1
    while low <= high:
        middle= (low+high)//2   
         #if target is in middle
        if arr[middle]== target:
            return middle    
       #if target is smaller than the middle value,
       #target would be on the left of the search tree
       #Search range would be: low=0, high= (middle-1 )            
        elif arr[middle]>target:
            high = middle-1
        #if target is larger than the middle value,
        # it wouuld be on the right of the search tree
        #Search range would be: low=middle+1, high= (len(arr)-1)
        # low  would be more than middle  
        elif arr[middle]<target:
            low = middle+1 

    return -1  # not found
