class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        transformed_nums = set(nums)
        longest_length = 0

        for num in transformed_nums:

            if (num - 1) not in transformed_nums:
                current = num
                repeated_count = 1
                while (current + 1) in transformed_nums:
                    current = current + 1
                    repeated_count += 1
                
                longest_length = max(longest_length, repeated_count)

        return longest_length




