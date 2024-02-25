# Linear Search

def linear_search(A, v):
    for i in range(len(A)):
        if A[i] == v:
            return i
    return None

print(linear_search([3,4,6,78,9,2,1,4,5,6], 1))