"""3555. 排序每个滑动窗口中最小的子数组"""


class Solution:
    def minSubarraySort(self, nums: list[int], k: int) -> list[int]:
        answer = []
        for start in range(len(nums) - k + 1):
            window = nums[start : start + k]
            ordered = sorted(window)
            left = next(
                (i for i, (a, b) in enumerate(zip(window, ordered)) if a != b), k
            )
            right = next(
                (
                    i
                    for i, (a, b) in enumerate(zip(window[::-1], ordered[::-1]))
                    if a != b
                ),
                k,
            )
            answer.append(0 if left == k else k - left - right)
        return answer


if __name__ == "__main__":
    test_cases = [
        (([1, 3, 2, 4, 5], 3), [2, 2, 0]),
        (([5, 4, 3, 2, 1], 4), [4, 4]),
    ]
    for _, ((nums, k), expected) in enumerate(test_cases):
        assert Solution().minSubarraySort(nums, k) == expected
