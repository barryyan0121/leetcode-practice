"""2412. 完成所有交易的初始最少钱数"""


class Solution:
    def minimumMoney(self, transactions: list[list[int]]) -> int:
        loss = sum(max(0, cost - cashback) for cost, cashback in transactions)
        return loss + max(min(cost, cashback) for cost, cashback in transactions)


if __name__ == "__main__":
    test_cases = [(([[2, 1], [5, 0]],), 7)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minimumMoney(*args) == expected
