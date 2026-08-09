class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result=""
        for i in range(len(strs[0])):
            x=strs[0][i]
            for string in strs:
                if i==len(string) or x!=string[i]:
                    return result
            result+=x
        return result
        