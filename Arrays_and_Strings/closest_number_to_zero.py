"""
Given an integer array nums of size n, return the number with the value 
closest to 0 in nums. If there are multiple answers, return the number with the largest value.

"""

nums = [2,-1,1]
def close_to_zero():
    close = nums[0]
    for i in nums:
        if abs(i) < abs(close):
            close = i
        
    if close < 0 and abs(close) in nums:
        return abs(close)
    else:
        return close

print(close_to_zero())

"""
Time complexity = O(n)


"""