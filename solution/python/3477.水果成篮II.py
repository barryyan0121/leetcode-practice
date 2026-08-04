"""3477. 水果成篮 II"""


class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        """Return the number of fruit types that cannot be placed."""
        used = [False] * len(baskets)
        unplaced = 0
        for fruit in fruits:
            for i, capacity in enumerate(baskets):
                if not used[i] and capacity >= fruit:
                    used[i] = True
                    break
            else:
                unplaced += 1
        return unplaced


test_cases = [
    (([4, 2, 5], [3, 5, 4]), 1),
    (([3, 6, 1], [6, 4, 7]), 0),
]


if __name__ == "__main__":
    for case_index, ((fruits, baskets), expected) in enumerate(test_cases):
        actual = Solution().numOfUnplacedFruits(fruits, baskets)
        assert actual == expected, (case_index, fruits, baskets, actual, expected)
    print("all tests passed")
