A = [1,5,5,2,6,8,10,99,90,100,101,99,110,120,130,110,122,121,90,91,990,100,120,129,55]
debug = False

def solution(A):
    """
    This is the naive solution to the stated problem.
    It has a complexity of O((len(A))**2)
    """
    maxi = 0
    for starting_point in range(len(A)):
        pos_1 = frog1(A,starting_point)
        pos_2 = frog2(A,starting_point)
        
        distance = pos_2 - pos_1 + 1 # distance between two frogs
        
        if debug:
            print(f"pos_1 = {pos_1}")
            print(f"pos_2 = {pos_2}")
            print(f"distance = {distance}")
        
        if distance > maxi:
            maxi = distance
            position = starting_point
    return maxi,position
 
   
def frog1(A, starting_point):
    """
    Function that returns the position of the frog 
    that goes to the left from starting_position
    """
    curr = starting_point
    if starting_point == 0:
        return 0
    while A[curr]<=A[curr-1]:
        curr+=-1
        if curr == 0:
            break
    return curr
    
def frog2(A, starting_point):
    """
    Function that return the position of the frog 
    that goes to the right from starting_position
    """
    curr = starting_point
    if starting_point == len(A)-1:
        return len(A)-1
    while A[curr]<=A[curr+1] :
        curr+=1
        if curr == len(A)-1:
            break
    return curr
    
print(solution(A))