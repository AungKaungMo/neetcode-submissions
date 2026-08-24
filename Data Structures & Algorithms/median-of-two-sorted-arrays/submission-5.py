class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        
        mid = len(nums) // 2
        isEven = len(nums) % 2 == 0
        for num in nums:
            if not isEven:
                return float(nums[mid])
            else:
                return float((nums[mid] + nums[mid -1]) / 2)