"""3072. 将元素分配到两个数组中 II"""


class Fenwick:
    def __init__(self, size: int) -> None:
        self.tree = [0] * (size + 1)

    def add(self, index: int, delta: int) -> None:
        while index < len(self.tree):
            self.tree[index] += delta
            index += index & -index

    def query(self, index: int) -> int:
        total = 0
        while index:
            total += self.tree[index]
            index -= index & -index
        return total


class Solution:
    def resultArray(self, nums: list[int]) -> list[int]:
        values = sorted(set(nums))
        rank = {value: index + 1 for index, value in enumerate(values)}

        first = [nums[0]]
        second = [nums[1]]
        tree1 = Fenwick(len(values))
        tree2 = Fenwick(len(values))
        tree1.add(rank[nums[0]], 1)
        tree2.add(rank[nums[1]], 1)

        for value in nums[2:]:
            idx = rank[value]
            greater1 = len(first) - tree1.query(idx)
            greater2 = len(second) - tree2.query(idx)
            if greater1 > greater2 or (
                greater1 == greater2 and len(first) <= len(second)
            ):
                first.append(value)
                tree1.add(idx, 1)
            else:
                second.append(value)
                tree2.add(idx, 1)
        return first + second


if __name__ == "__main__":
    test_cases = [
        ([2, 1, 3, 3], [2, 3, 1, 3]),
        ([5, 14, 3, 1, 2], [5, 3, 1, 2, 14]),
        ([3, 3, 3, 3], [3, 3, 3, 3]),
    ]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().resultArray(nums) == expected
