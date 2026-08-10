class Solution:
    def palindrome(self,s, left, right):
            max_arr = ""

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > len(max_arr):
                    max_arr = s[left:right + 1]

                left -= 1
                right += 1

            return max_arr

    def longestPalindrome(self, s: str) -> str:
            best = ""

            for i in range(len(s)):
                odd = self.palindrome(s, i, i)
                even = self.palindrome(s, i, i + 1)

                if len(odd) > len(best):
                    best = odd

                if len(even) > len(best):
                    best = even

            return best
                