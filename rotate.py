def left_rotate(arr, k):
    k = k % len(arr) 
    rotated = arr[k:] + arr[:k]
    return rotated

# Example usage
arr = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter k (rotation step): "))

print("Left Rotated Array:", left_rotate(arr, k))
