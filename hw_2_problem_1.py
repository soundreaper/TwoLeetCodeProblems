"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""

"""
Okay, so I want to be able to process both positive and negative numbers from the problem statement. I also
have to return the INDEX and not the actual number itself. I also cannot use the same element again. I believe
the easiest way to do this problem would be to find the compliment to whatever number is selected in the array.
"""

def twoSum(nums, target):
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]

nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))