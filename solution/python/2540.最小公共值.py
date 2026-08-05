"""2540. 最小公共值"""


class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        first = second = 0
        while first < len(nums1) and second < len(nums2):
            if nums1[first] == nums2[second]:
                return nums1[first]
            if nums1[first] < nums2[second]:
                first += 1
            else:
                second += 1
        return -1


if __name__ == "__main__":
    test_cases = [(([1, 2, 3], [2, 4]), 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().getCommon(*args) == expected
