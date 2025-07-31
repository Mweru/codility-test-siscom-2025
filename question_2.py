"""
**LONGEST PALINDROMIC SUBSTRING**

Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters."""


"#Solution"
        
def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """

    def expand_from_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    if not s or len(s) == 1:
        return s

    longest = ""
    for i in range(len(s)):
        odd = expand_from_center(i, i)
        even = expand_from_center(i, i + 1)

        current_longest = odd if len(odd) > len(even) else even

        if len(current_longest) > len(longest):
            longest = current_longest

    return longest
