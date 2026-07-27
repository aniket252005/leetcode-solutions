class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        freq = {}

        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        for char in t:
            if char in freq:
                freq[char] -= 1
            else:
                freq[char] = -1

        for count in freq.values():
            if count != 0:
                return False

        return True