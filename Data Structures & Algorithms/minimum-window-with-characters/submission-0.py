class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""

        t_count = {}

        for i in t:
            t_count[i] = t_count.get(i, 0) + 1
        
        have = len(t_count)
        window = {}
        res = (float("inf"), 0, 0)
        left = 0
        formed = 0

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in t_count and window[c] == t_count[c]:
                formed += 1
            
            while left <= right and formed == have:
                if (right - left + 1) < res[0]:
                    res = (right - left + 1, left, right)

                lc = s[left]
                window[lc] -= 1
                if lc in t_count and window[lc] < t_count[lc]:
                    formed -= 1
                
                left += 1
        
        return "" if res[0] == float("inf") else s[res[1] : res[2] + 1]