"""2019. 解出数学表达式的学生分数"""


class Solution:
    def scoreOfStudents(self, s: str, answers: list[int]) -> int:
        nums = list(map(int, s[::2]))
        ops = s[1::2]
        n = len(nums)
        dp = [[set() for _ in range(n)] for _ in range(n)]
        for i, value in enumerate(nums):
            dp[i][i].add(value)
        for length in range(2, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1
                for mid in range(left, right):
                    for a in dp[left][mid]:
                        for b in dp[mid + 1][right]:
                            value = a + b if ops[mid] == "+" else a * b
                            if value <= 1000:
                                dp[left][right].add(value)
        correct = 0
        term = nums[0]
        for i, op in enumerate(ops):
            if op == "*":
                term *= nums[i + 1]
            else:
                correct += term
                term = nums[i + 1]
        correct += term
        possible = dp[0][-1]
        return sum(
            5 if answer == correct else 2 if answer in possible else 0
            for answer in answers
        )


if __name__ == "__main__":
    test_cases = [(("7+3*1*2", [20, 13, 42]), 7)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().scoreOfStudents(*args) == expected
