class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_hash = {}
        res_hash = {}

        for i in range(len(s1)):
            s1_hash[s1[i]] = s1_hash.get(s1[i], 0) + 1
            res_hash[s2[i]] = res_hash.get(s2[i], 0) + 1

        if s1_hash == res_hash:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            res_hash[s2[r]] = res_hash.get(s2[r], 0) + 1

            res_hash[s2[l]] -= 1

            if res_hash[s2[l]] == 0:
                del res_hash[s2[l]]

            l += 1

            if s1_hash == res_hash:
                return True
        
        return False
        