class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result, i = [], 0
        #  [48,24,12,8]   
        while i < len(nums):

            total = 1
            for key, val in enumerate(nums):
                if i != key:
                    total = total * val
                
            result.append(total)
            total = 1
            i += 1

        return result
                



        