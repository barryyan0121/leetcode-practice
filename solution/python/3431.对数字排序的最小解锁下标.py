class Solution:
    def minUnlockedIndices(self, nums: list[int], locked: list[int]) -> int:
        n = len(nums)
        first2 = first3 = n
        last1 = last2 = -1
        for i, value in enumerate(nums):
            if value == 1:
                last1 = i
            elif value == 2:
                first2 = min(first2, i)
                last2 = i
            else:
                first3 = min(first3, i)
        if first3 < last1:
            return -1
        return sum(
            locked[i] and (first2 <= i < last1 or first3 <= i < last2) for i in range(n)
        )


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 1, 2, 3, 2], [1, 0, 1, 1, 0, 1]), 0),
        (([1, 2, 1, 1, 3, 2, 2], [1, 0, 1, 1, 0, 1, 0]), 2),
        (([1, 2, 1, 2, 3, 2, 1], [0] * 7), -1),
    ]
    for _, ((nums, locked), expected) in enumerate(test_cases):
        assert Solution().minUnlockedIndices(nums, locked) == expected
