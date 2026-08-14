class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

        result = []
        sorted_count = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
        for i, key in enumerate(sorted_count):
            if i < k:
                result.append(key)

        return result