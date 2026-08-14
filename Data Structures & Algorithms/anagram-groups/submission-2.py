class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # mapping character count of each string to list of Anagrams

        for s in strs :
            count = [0] * 26 # a - z

            for c in s:
                count[ord(c) - ord("a")] += 1 # ord returns the ASCII value

            result[tuple(count)].append(s)
        # O(m * n) solution

        return list(result.values())

