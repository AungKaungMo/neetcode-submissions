class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = []
        for i in range(len(tokens)):
            if tokens[i] in "+-*/":
                a, b = result.pop(), result.pop()
                if tokens[i] == "+":
                        result.append(a + b)
                elif tokens[i] == "-":
                        result.append(b - a)
                elif tokens[i] == "*":
                        result.append(a * b)
                elif tokens[i] == "/":
                        result.append(int(float(b) / a))
            else:
                result.append(int(tokens[i]))
        
        return result[0]