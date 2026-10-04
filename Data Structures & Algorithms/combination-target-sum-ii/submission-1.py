class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        curr = []
        candidates.sort()

        def dfs(idx, path, total):
            if total == target:
                curr.append(path.copy())
                return
            
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if total > target: 
                    break
                
                path.append(candidates[i])
                dfs(i + 1, path, total + candidates[i])
                path.pop()
        
        dfs(0, [], 0)
        return curr