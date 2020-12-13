def max_sum(arr):
    """
    Given an array of integers, find the subset of non-adjacent elements with the maximum sum
    """
    #edge case elimination
    if len(arr) == 0:
        return 0
    
    inc_total=0
    exc_total=0

    for num in arr:
        new_exc_total= max(inc_total, exc_total)

        inc_total=exc_total + num
        exc_total =new_exc_total
    
    return max(inc_total, exc_total)


    

