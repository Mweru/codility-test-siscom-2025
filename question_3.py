"""
**SUBSTRING WITH CONCATENATION OF ALL WORDS**

You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]

Output: [0,9]

Explanation:

The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

Output: []

Explanation:

There is no concatenated substring.

Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

Output: [6,9,12]

Explanation:

The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].

 

Constraints:

1 <= s.length <= 104
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters.

"""

"#Solution"


def findSubstring(s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
    if not s or not words or not words[0]:
    return []

    word_len = len(words[0])
    total_len = word_len * len(words)
    n = len(s)
    result = []

    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    for i in range(word_len):
        left = i
        right = i
        window_count = {}
        count = 0

        while right + word_len <= n:
            word = s[right:right + word_len]
            right += word_len

            if word in word_count:
                window_count[word] = window_count.get(word, 0) + 1
                count += 1

                while window_count[word] > word_count[word]:
                    left_word = s[left:left + word_len]
                    window_count[left_word] -= 1
                    count -= 1
                    left += word_len

                if count == len(words):
                    result.append(left)
            else:
                window_count.clear()
                count = 0
                left = right

    return result