# 242. Valid Anagram
# Easy
# 9.2K
# 290
# Companies
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:


# Input: s = "rat", t = "car"
# Output: false
def isAnagram(self, s: str, t: str) -> bool:
    s = sorted(list(s))
    t = sorted(list(t))
    if len(s) != len(t):
        return False
    else:
        for i in range(len(s)):
            if s[i] != t[i]:
                return False
    return True
