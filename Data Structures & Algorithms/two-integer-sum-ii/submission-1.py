class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_list = {}

        for key, num in enumerate(numbers):
            x = target - num

            if x in num_list:
                return [num_list.get(x), key + 1]

            num_list[num] = key + 1
        
        return []