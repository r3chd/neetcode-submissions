class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in range(len(numbers)):
            if (target - numbers[i]) in numbers:
                indexTarget = target - numbers[i]
                
                for j in range(len(numbers)):
                    if numbers[j] == indexTarget: 
                        result = [i + 1, j + 1]

                        return result