class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(i, string):
            if len(string) == len(digits):
                result.append(string)
                return
            for c in digitToChar[digits[i]]:
                backtrack(i+1, string + c)

        if digits:
            backtrack(0, "")

        return result
                