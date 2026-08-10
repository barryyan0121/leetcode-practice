"""3002. 移除后集合的最多元素数"""


class Solution:
    def maximumSetSize(self, nums1: list[int], nums2: list[int]) -> int:
        first, second = set(nums1), set(nums2)
        only_first = len(first - second)
        only_second = len(second - first)
        common = len(first & second)
        capacity = min(len(nums1) // 2, only_first) + min(len(nums2) // 2, only_second)
        return min(len(nums1) // 2 + len(nums2) // 2, capacity + common)


if __name__ == "__main__":
    assert Solution().maximumSetSize([1, 2, 1, 2], [1, 1, 1, 1]) == 2
