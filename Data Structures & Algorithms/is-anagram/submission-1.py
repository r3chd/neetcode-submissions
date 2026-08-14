from collections import Counter

# alternative solution using built in python library collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

            