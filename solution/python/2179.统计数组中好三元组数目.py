"""2179. 统计数组中好三元组数目"""


class Fenwick:
    def __init__(self, size: int):
        self.tree = [0] * (size + 1)

    def add(self, index: int, value: int) -> None:
        index += 1
        while index < len(self.tree):
            self.tree[index] += value
            index += index & -index

    def sum(self, index: int) -> int:
        total = 0
        while index:
            total += self.tree[index]
            index -= index & -index
        return total


class Solution:
    def goodTriplets(self, nums1: list[int], nums2: list[int]) -> int:
        position = {value: index for index, value in enumerate(nums2)}
        mapped = [position[value] for value in nums1]
        n = len(mapped)
        left_tree = Fenwick(n)
        right_tree = Fenwick(n)
        for value in mapped:
            right_tree.add(value, 1)
        answer = 0
        for value in mapped:
            right_tree.add(value, -1)
            left = left_tree.sum(value)
            right = right_tree.sum(n) - right_tree.sum(value + 1)
            answer += left * right
            left_tree.add(value, 1)
        return answer


if __name__ == "__main__":
    assert Solution().goodTriplets([2, 0, 1, 3], [0, 1, 2, 3]) == 1
