class Solution:
    def characterReplacement(self, strs: str, k: int) -> int:
        count = {}
        l = 0
        max_freq = 0
        max_length = 0

        for r in range(len(strs)):

            count[strs[r]] = count.get(strs[r], 0) + 1

            max_freq = max(max_freq, count[strs[r]])

            while (r - l + 1) - max_freq > k:
                count[strs[l]] -= 1
                l += 1
            
            max_length = max(max_length, r - l + 1)

        return max_length

    