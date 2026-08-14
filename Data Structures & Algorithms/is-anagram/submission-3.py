class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def countChars(string):
            count = {}
            for char in string:
                if char not in count:
                    count[char] = 1
                else:
                    count[char] += 1
            
            return count
        
        sCount = countChars(s)
        tCount = countChars(t)

        if sCount == tCount:
            return True
        else:
            return False
