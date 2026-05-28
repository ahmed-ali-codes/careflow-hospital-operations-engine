def merge_sort(arr, key=lambda x: x):
    """Modified Merge Sort to support custom key functions."""
    
    # Base case: if array has 0 or 1 element, it is already sorted
    if len(arr) <= 1:
        return arr
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key)   # Recursively sort left half
    right = merge_sort(arr[mid:], key)  # Recursively sort right half
    
    # Merge step: combine two sorted halves into one sorted list
    res = []
    i = j = 0
    
    # Compare elements from both halves using the key function
    while i < len(left) and j < len(right):
        if key(left[i]) < key(right[j]):
            res.append(left[i])  # Add smaller element
            i += 1
        else:
            res.append(right[j])
            j += 1
            
    # Add any remaining elements from left or right
    res.extend(left[i:])
    res.extend(right[j:])
    
    return res  # Return merged sorted array


def quick_sort(arr, key=lambda x: x):
    """Modified Quick Sort to support custom key functions."""
    
    # Base case: if array has 0 or 1 element, it is already sorted
    if len(arr) <= 1:
        return arr
    
    # Select pivot element (middle element)
    pivot = arr[len(arr) // 2]
    
    # Partition the array into three parts based on pivot
    # Use key function for comparison
    left = [x for x in arr if key(x) < key(pivot)]      # Elements less than pivot
    middle = [x for x in arr if key(x) == key(pivot)]   # Elements equal to pivot
    right = [x for x in arr if key(x) > key(pivot)]     # Elements greater than pivot
    
    # Recursively sort left and right parts and combine results
    return quick_sort(left, key) + middle + quick_sort(right, key)