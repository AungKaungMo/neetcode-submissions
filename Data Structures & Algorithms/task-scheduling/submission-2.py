class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = [0] * 26
        for task in tasks:
            counts[ord(task) - ord('A')] += 1
        
        maxf = max(counts)
        maxCount = 0

        for c in counts:
            maxCount += 1 if c == maxf else 0
        
        time = (maxf - 1) * (n + 1) + maxCount
        return max(len(tasks), time)