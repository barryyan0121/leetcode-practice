"""2561. 重排水果"""


class Solution:
    def minCost(self, basket1: list[int], basket2: list[int]) -> int:
        from collections import Counter

        first, second = Counter(basket1), Counter(basket2)
        all_counts = first + second
        if any(count % 2 for count in all_counts.values()):
            return -1
        extra1, extra2 = [], []
        for value, count in all_counts.items():
            diff = first[value] - second[value]
            (extra1 if diff > 0 else extra2).extend([value] * (abs(diff) // 2))
        minimum = min(all_counts)
        extra1.sort()
        extra2.sort(reverse=True)
        return sum(min(a, b, 2 * minimum) for a, b in zip(extra1, extra2))


if __name__ == "__main__":
    test_cases = [(([4, 2, 2, 2], [1, 4, 1, 2]), 1)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minCost(*args) == expected
