"""2489. 固定比率的子字符串数"""


class Solution:
    def fixedRatio(self, s: str, num1: int, num2: int) -> int:
        counts = {0: 1}
        balance = answer = 0
        for char in s:
            balance += num2 if char == "0" else -num1
            answer += counts.get(balance, 0)
            counts[balance] = counts.get(balance, 0) + 1
        return answer
