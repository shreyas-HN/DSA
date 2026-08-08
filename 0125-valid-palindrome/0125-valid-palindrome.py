class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid="".join(i for i in s if i.isalnum())
        lvalid=valid.lower()
        return lvalid==lvalid[::-1]


        