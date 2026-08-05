"""2144. 购买糖果的最低成本"""


class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        cost.sort(reverse=True)
        return sum(value for index, value in enumerate(cost) if index % 3 != 2)


if __name__ == "__main__":
    test_cases = [(([1, 2, 3],), 5), (([6, 5, 7, 9, 2, 2],), 23)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minimumCost(*args) == expected
