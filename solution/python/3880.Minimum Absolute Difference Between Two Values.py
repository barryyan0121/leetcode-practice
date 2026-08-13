class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        best = float("inf")
        index1 = -1
        index2 = -1
        for index, value in enumerate(nums):
            if value == 1:
                index1 = index
            elif value == 2:
                index2 = index
            else:
                continue
            if index1 != -1 and index2 != -1:
                best = min(best, abs(index1 - index2))
        return best if best != float("inf") else -1


if __name__ == "__main__":
    test_cases = [
        ([1, 0, 0, 2, 0, 1], 2),
        ([1, 0, 1, 0], -1),
    ]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().minAbsoluteDifference(nums) == expected
