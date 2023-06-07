# Subarray Sum size k
# Given an array, find the average of each subarray of ‘K’ contiguous elements in it.
# Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
# Here, we are asked to find the average of all subarrays of '5' contiguous elements in the given array. Let's solve this:
# 	1. For the first 5 numbers (subarray from index 0-4), the average is:  (1+3+2+6-1)/5 = 2.2
# 	2. The average of next 5 numbers (subarray from index 1-5) is:  (3+2+6-1+4)/5 = 2.8
# 	3. For the next 5 numbers (subarray from index 2-6), the average is:  (2+6-1+4+1)/5 = 2.4

# Output: [2.2, 2.8, 2.4, 3.6, 2.8]


def subarraySum(nums, k):
    windowStart = 0
    arr = []
    windowSum = 0
    for windowEnd in range(len(nums)):
        windowSum += nums[windowEnd]
        if windowEnd >= k - 1:
            arr.append(windowSum / k)
            windowSum -= nums[windowStart]
            windowStart += 1
    return arr


nums = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5
print(subarraySum(nums, k))
