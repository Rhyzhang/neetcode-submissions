class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        state = True
        if len(s) == len(t):
            for i in range(len(s)):
                if s[i] != t[i]:
                    state = False
        else:
            state = False
        
        return state
        