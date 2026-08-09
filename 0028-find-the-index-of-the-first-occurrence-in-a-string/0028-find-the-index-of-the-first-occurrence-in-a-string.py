class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        k = len(needle)

        while i <= len(haystack) - k:
            if haystack[i:i+k] == needle:
                return i
            else:
                i += 1

        return -1


            