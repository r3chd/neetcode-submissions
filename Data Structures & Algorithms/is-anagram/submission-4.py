class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def countChars(string):
            count = {}
            for s in string:
                if s not in count:
                    count[s] = 1
                else:
                    count[s] += 1
            return count
        
        return (countChars(s) == countChars(t))