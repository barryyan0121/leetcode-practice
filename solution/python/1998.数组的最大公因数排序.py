"""1998. 数组的最大公因数排序"""

from math import gcd


class Solution:
    def gcdSort(self, nums: list[int]) -> bool:
        parent = list(range(max(nums) + 1))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> None:
            a, b = find(a), find(b)
            if a != b:
                parent[a] = b

        for value in nums:
            factor = 2
            x = value
            while factor * factor <= x:
                if x % factor == 0:
                    union(value, factor)
                    while x % factor == 0:
                        x //= factor
                factor += 1
            if x > 1:
                union(value, x)
        return all(find(a) == find(b) for a, b in zip(nums, sorted(nums)))


if __name__ == "__main__":
    test_cases = [(([7, 21, 3],), True), (([5, 2, 6, 2],), False)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().gcdSort(*args) == expected
