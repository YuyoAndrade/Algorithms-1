# First try to implement Merge Sort

def merge(le, re):
    A = [] # Create empty array
    i, j = 0, 0 # Initialize pointers
    while len(le) > i and len(re) > j: # While there are remaining cards (numbers) on both continue.
        if le[i] > re[j]: # If the left side is bigger than the right, append the right
            A.append(re[j])
            j += 1 # Get new card (add 1 to the right side pointer)
        else: # Else append the left
            A.append(le[i])
            i += 1 # # Get new card (add 1 to the left side pointer)
    if len(le) > i: # If there are remaining cards on the left side, append all
        A += le[i:]
    else: # Else append all right side cards
        A += re[j:]
    return A # Return sorted array

# First recursively divide left and right
def merge_sort(A):
    m = int(len(A) / 2) # Divide in half
    if m == 0: # If there is no more division return (length 1)
        return A

    le = merge_sort(A[:m]) # Continiously divide the left side
    re = merge_sort(A[m:]) # Continiously divide the right side
    A = merge(le, re) # Sort left and right side

    return A


A = [4, 8, 1, 2, 2, 3, 7, 3]
print("Unsorted: ", A)
print(merge_sort(A))