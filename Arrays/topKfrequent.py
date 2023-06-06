# Top K Frequent Elements
# Medium
# 14.6K
# 515
# Companies
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:


# Input: nums = [1], k = 1
# Output: [1]
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        freq = [[] for i in range(len(nums) + 1)]
        for key, val in d.items():
            freq[val].append(key)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
