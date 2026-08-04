"""3479. 水果成篮 III"""


class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        wextranide = (fruits, baskets)
        size = len(baskets)
        base = 1
        while base < size:
            base *= 2
        tree = [0] * (2 * base)
        tree[base : base + size] = baskets
        for i in range(base - 1, 0, -1):
            tree[i] = max(tree[2 * i], tree[2 * i + 1])

        def take_first_at_least(value: int) -> bool:
            if tree[1] < value:
                return False
            node = 1
            left = 0
            right = size
            while node < base:
                middle = (left + right) // 2
                if tree[2 * node] >= value:
                    node *= 2
                    right = middle
                else:
                    node = 2 * node + 1
                    left = middle
            tree[node] = 0
            node //= 2
            while node:
                tree[node] = max(tree[2 * node], tree[2 * node + 1])
                node //= 2
            return True

        return sum(not take_first_at_least(fruit) for fruit in fruits)


if __name__ == "__main__":
    test_cases = [
        (([4, 2, 5], [3, 5, 4]), 1),
        (([3, 6, 1], [6, 4, 7]), 0),
    ]
    for _, ((fruits, baskets), expected) in enumerate(test_cases):
        assert Solution().numOfUnplacedFruits(fruits, baskets) == expected
