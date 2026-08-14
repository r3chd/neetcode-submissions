class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        s_count = self.createDict(s)
        t_count = self.createDict(t)
        if t_count != s_count:
            return False
        
        return True

    def createDict(self, x: str) -> dict:
        my_dict = {}
        for char in x:
            if char not in my_dict:
                my_dict[char] = 1
            else:
                my_dict[char] += 1
        return my_dict
            