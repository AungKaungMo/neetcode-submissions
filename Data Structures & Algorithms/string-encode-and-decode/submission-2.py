class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        result = []
        for s in strs:
            result.append(str(len(s)))
            result.append('#')
            result.append(s)
        
        return "".join(result)

    def decode(self, strs: str) -> List[str]:
        if not strs:
            return []

        result, i = [], 0

        while i < len(strs):
            j = i
            while strs[j] != '#':
                j += 1
            
            length = int(strs[i:j])
            i = j + 1
            j = length + i
            result.append(strs[i:j])
            i = j

        return result



        