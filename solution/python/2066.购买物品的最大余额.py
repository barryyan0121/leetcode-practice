"""2066. 购买物品的最大余额"""


class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        return 100 - ((purchaseAmount + 5) // 10) * 10


if __name__ == "__main__":
    test_cases = [((9,), 90), ((15,), 80)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().accountBalanceAfterPurchase(*args) == expected
