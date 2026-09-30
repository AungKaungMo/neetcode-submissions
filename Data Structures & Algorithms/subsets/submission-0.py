class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subnet = []

        def dfs(i):
            if i >= len(nums):
                res.append(subnet.copy())
                return
            
            subnet.append(nums[i])
            dfs(i + 1)
            subnet.pop()
            dfs(i + 1)

        dfs(0)
        return res