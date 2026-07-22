class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_map = {}

        for i, num in enumerate(nums):
            x = target - num
            if x in sum_map:
                return [sum_map[x], i]
            
            sum_map[num] = i
        
        return []
        