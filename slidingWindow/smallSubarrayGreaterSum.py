# Smallest Subarray With a Greater Sum
# Given an array of positive integers and a number ‘S,’ find the length of the smallest contiguous subarray whose sum is greater than or equal to 'S'. Return 0 if no such subarray exists.
# Example 1:
# Input: [2, 1, 5, 2, 3, 2], S=7
# Output: 2
# Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].
# Example 2:
# Input: [2, 1, 5, 2, 8], S=7
# Output: 1
# Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
# Example 3:
# Input: [3, 4, 1, 1, 6], S=8
# Output: 3
# Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].
import math


def smallSubarryaGreaterSum(nums, S):
    windowStart = 0
    windowSum = 0
    minL = math.inf
    for windowEnd in range(len(nums)):
        windowSum += nums[windowEnd]
        while windowSum >= S:
            minL = min(minL, windowEnd - windowStart + 1)
            windowSum -= nums[windowStart]
            windowStart += 1

    return minL


nums = [2, 1, 5, 2, 8]
S = 7
print(smallSubarryaGreaterSum(nums, S))
