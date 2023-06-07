# Longest Substring with K Distinct Characters
# Given a string, find the length of the longest substring in it with no more than K distinct characters.
# You can assume that K is less than or equal to the length of the given string.
# Example 1:
# Input: String="araaci", K=2
# Output: 4
# Explanation: The longest substring with no more than '2' distinct characters is "araa".
# Example 2:
# Input: String="araaci", K=1
# Output: 2
# Explanation: The longest substring with no more than '1' distinct characters is "aa".
# Example 3:
# Input: String="cbbebi", K=3
# Output: 5
# Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
def LongestSubstringwithKDistinctCharacters(s, K):
    windowStart = 0
    windowSum = 0
    d = {}
    maxL = 0
    for windowEnd in range(len(s)):
        if s[windowEnd] in d:
            d[s[windowEnd]] += 1
        else:
            d[s[windowEnd]] = 1

        while len(d) > K:
            d[s[windowStart]] -= 1
            if d[s[windowStart]] == 0:
                del d[s[windowStart]]
            windowStart += 1
            maxL = max(maxL, windowEnd - windowStart + 1)
    return maxL


s = "araaci"
K = 2
print(LongestSubstringwithKDistinctCharacters(s, K))
