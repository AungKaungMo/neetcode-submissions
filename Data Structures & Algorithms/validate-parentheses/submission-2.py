class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for i in s:
            if i in matching_map:
                if stack and stack[-1] == matching_map[i]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(i)
        
        return len(stack) == 0