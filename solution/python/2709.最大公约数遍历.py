"""2709. 最大公约数遍历"""


class Solution:
    def canTraverseAllPairs(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return True
        if 1 in nums:
            return False
        parent = list(range(len(nums)))

        def find(node: int) -> int:
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        def union(left: int, right: int) -> None:
            left, right = find(left), find(right)
            if left != right:
                parent[left] = right

        factors = {}
        for index, number in enumerate(nums):
            divisor = 2
            while divisor * divisor <= number:
                if number % divisor == 0:
                    factors.setdefault(divisor, index)
                    union(index, factors[divisor])
                    while number % divisor == 0:
                        number //= divisor
                divisor += 1
            if number > 1:
                factors.setdefault(number, index)
                union(index, factors[number])
        root = find(0)
        return all(find(index) == root for index in range(len(nums)))


if __name__ == "__main__":
    assert Solution().canTraverseAllPairs([2, 3, 6])
    assert not Solution().canTraverseAllPairs([3, 9, 5])
