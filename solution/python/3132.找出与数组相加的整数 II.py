class Solution:
    def minimumAddedInteger(self, nums1: list[int], nums2: list[int]) -> int:
        nums1.sort()
        nums2.sort()
        answer = float("inf")
        for index in range(3):
            addition = nums2[0] - nums1[index]
            first = index
            second = 0
            removed = index
            while first < len(nums1) and second < len(nums2):
                if nums1[first] + addition == nums2[second]:
                    first += 1
                    second += 1
                else:
                    first += 1
                    removed += 1
            if second == len(nums2):
                answer = min(answer, addition)
        return answer


if __name__ == "__main__":
    test_cases = [([4, 20, 16, 12, 8], [14, 18, 10], -2), ([3, 5, 5, 3], [7, 7], 2)]
    for _, (nums1, nums2, expected) in enumerate(test_cases):
        assert Solution().minimumAddedInteger(nums1, nums2) == expected
