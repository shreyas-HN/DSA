class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=0
        longest=0
        d={}
        while j < len(s):
            if s[j] not in d:
                d[s[j]] = j
            else:
                i = max(i, d[s[j]] + 1)
                d[s[j]] = j

            j += 1

            count = j - i
            longest = max(longest, count)

        return longest


                        