class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=0
        longest=0
        count=0
        se=set()
        while j<len(s) and i<len(s):
            if s[j] not in se:
                se.add(s[j])
                count=(j-i)+1
                j += 1
            else:
                se.remove(s[i])
                i+=1
            longest=max(longest,count)
        return longest
                