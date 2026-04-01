class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        charS = {}
        for char in s:
            charS[char] = charS.get(char,0) + 1
         
        charT = {}
        for char in t:
            charT[char] = charT.get(char,0) + 1
        return charS == charT
