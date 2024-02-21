# Insertion Sort

def insertion_sort(A):
    for j in range(1, len(A)): # Start from index 1 since the first time is already ordered.
        key = A[j] # Store current value
        i = j - 1 # Pointer to left value
        while i >= 0 and A[i] > key: # Check if the number on the left is smaller than key or end of line.
            A[i + 1] = A[i] # Move value to the right
            i -= 1 #
        A[i+1] = key # Insert key once it is the smallest value or the left is smallest
    return A


A = [4, 8, 1, 2, 2, 3, 7, 3]

print(insertion_sort(A))