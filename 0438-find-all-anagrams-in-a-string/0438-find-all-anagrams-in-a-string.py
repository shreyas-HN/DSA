class Solution:
    def dictionarygenerator(self, string):
        d = {}

        for char in string:
            if char not in d:
                d[char] = 1
            else:
                d[char] += 1

        return d

    def findAnagrams(self, s: str, p: str):
        if len(p) > len(s):
            return []

        k = len(p)
        i = 0
        j = k
        result = []

        target = self.dictionarygenerator(p)
        window = self.dictionarygenerator(s[i:j])

        while True:

            # Check current window
            if target == window:
                result.append(i)

            # Last window reached
            if j == len(s):
                break

            # Remove outgoing character
            window[s[i]] -= 1

            if window[s[i]] == 0:
                del window[s[i]]

            # Add incoming character
            if s[j] not in window:
                window[s[j]] = 1
            else:
                window[s[j]] += 1

            # Move window
            i += 1
            j += 1

        return result