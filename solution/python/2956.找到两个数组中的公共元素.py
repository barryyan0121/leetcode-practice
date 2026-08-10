"""2956. 找到两个数组中的公共元素"""


class Solution:
    def findIntersectionValues(self, nums1: list[int], nums2: list[int]) -> list[int]:
        first, second = set(nums1), set(nums2)
        return [
            sum(value in second for value in nums1),
            sum(value in first for value in nums2),
        ]


if __name__ == "__main__":
    assert Solution().findIntersectionValues([4, 3, 2, 3, 1], [2, 2, 5, 2, 3, 6]) == [
        3,
        4,
    ]
