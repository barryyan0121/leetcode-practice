"""2355. 你能拿走的最大图书数量"""


class Solution:
    def maximumBooks(self, books: list[int]) -> int:
        stack = []
        dp = [0] * len(books)
        answer = 0
        for i, value in enumerate(books):
            while stack and books[stack[-1]] - stack[-1] >= value - i:
                stack.pop()
            if stack:
                length = i - stack[-1]
            else:
                length = i + 1
            first = value - length + 1
            if first > 0:
                total = (first + value) * length // 2
            else:
                total = value * (value + 1) // 2
            if stack:
                total += dp[stack[-1]]
            dp[i] = total
            answer = max(answer, dp[i])
            stack.append(i)
        return answer
