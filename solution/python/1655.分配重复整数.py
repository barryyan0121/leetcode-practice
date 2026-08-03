# @lc app=leetcode.cn id=1655 lang=python3


class Solution:
    def canDistribute(self, nums: list[int], quantity: list[int]) -> bool:
        from collections import Counter
        from functools import lru_cache

        counts = tuple(sorted(Counter(nums).values(), reverse=True))
        quantity.sort(reverse=True)

        @lru_cache(None)
        def search(index: int, remaining: tuple[int, ...]) -> bool:
            if index == len(quantity):
                return True
            amount = quantity[index]
            tried = set()
            for position, available in enumerate(remaining):
                if available >= amount and available not in tried:
                    tried.add(available)
                    updated = list(remaining)
                    updated[position] -= amount
                    updated.sort(reverse=True)
                    if search(index + 1, tuple(updated)):
                        return True
            return False

        return search(0, counts)


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.canDistribute, ([1, 1, 2, 2], [2, 2]), True),
        (solution.canDistribute, ([1, 2, 3, 4], [2]), False),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1655 题 "分配重复整数" 所有测试用例通过')
