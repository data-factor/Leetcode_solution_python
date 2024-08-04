"""
Given an array of integers nums and an integer target, return indices of the two numbers such that 
they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""


number = [-1,4,-5,5]
target = 0


def two_sum():
  for num in number:
    for nums in number:
      if number[num] + number[nums] == target:
        return number[num],number[nums]
      else:
        continue

#print(two_sum())

## Worst case is O(n*n)

## Using hash
def two_sum_hash():
    hash = {}
    for i,num in enumerate(number):
        if target - num in hash:
            return ([hash[target -  num],i])
        elif num not in hash:
           hash[num] = i 
           
print(two_sum_hash()) 
# Runs on O(n)
