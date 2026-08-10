"""2232. 向表达式添加括号后的最小结果"""


class Solution:
    def minimizeResult(self, expression: str) -> str:
        plus = expression.index("+")
        best = None
        answer = ""
        for left in range(plus):
            for right in range(plus + 1, len(expression)):
                a = int(expression[:left] or 1)
                b = int(expression[left:plus])
                c = int(expression[plus + 1 : right + 1])
                d = int(expression[right + 1 :] or 1)
                value = a * (b + c) * d
                if best is None or value < best:
                    best, answer = (
                        value,
                        expression[:left]
                        + "("
                        + expression[left : right + 1]
                        + ")"
                        + expression[right + 1 :],
                    )
        return answer
