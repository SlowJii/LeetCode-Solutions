"""
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

# Su dung Ky thuat Hai con tro (2 pointer) va Cua so truot (Sliding Window)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 # Con tro Trai
        result = 0 
        charSet = set() # Cua so (Window)
        for right in range(len(s)):
            if s[right] not in charSet:
                charSet.add(s[right])
                result = max(result, right - left + 1)
            else:
                # Sliding Window
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
                charSet.add(s[right])
        return result