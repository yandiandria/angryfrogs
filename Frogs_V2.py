A = [1,5,5,2,6,8,10,99,90,100,101,99,110,120,130,110,122,121,90,91,990,100,120,129,55]

def solution(A):
    """
    This solution uses the principle of pre-fix and post-fix sums 
    Its complexity is O(len(A))
    """
    T_right = compute_T_right(A)
    T_left = compute_T_left(A)
    D = [0]*len(A)

    for elem in range(len(A)):
        D[elem] = T_right[elem] + T_left[elem]

    return 1 + max(D)


def compute_T_right(A):
    """
    Function that returns a table named res.
    The frog that starts on block i and
    goes on the right  will move by res[i] blocks
    """
    res = [0]*len(A)
    for elem in range(len(A)-2, -1, -1):
        if A[elem] <= A[elem + 1]:
            res[elem] = res[elem+1] + 1
    return res


def compute_T_left(A):
    """
    Function that returns a table named res.
    The frog that starts on block i and
    goes on the left will move by res[i] blocks
    """
    res = [0]*len(A)
    for elem in range(1, len(A)):
        if A[elem-1] >= A[elem]:
            res[elem] = res[elem-1] + 1
    return res

 
print(solution(A))