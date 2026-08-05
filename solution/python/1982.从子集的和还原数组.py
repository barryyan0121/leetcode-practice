"""1982. 从子集的和还原数组"""

from collections import Counter


class Solution:
    def recoverArray(self, n: int, sums: list[int]) -> list[int]:
        sums.sort()

        def recover(values: list[int]) -> list[int]:
            if len(values) == 1:
                return []
            difference = values[1] - values[0]
            counts = Counter(values)
            without = []
            with_value = []
            for value in values:
                if counts[value]:
                    counts[value] -= 1
                    without.append(value)
                    counts[value + difference] -= 1
                    with_value.append(value + difference)
            if 0 in without:
                return recover(without) + [difference]
            return recover(with_value) + [-difference]

        return recover(sums)


if __name__ == "__main__":
    test_cases = [((2, [-3, -1, 0, 2]), [-3, 2])]
    for _, (args, expected) in enumerate(test_cases):
        assert sorted(Solution().recoverArray(*args)) == expected
