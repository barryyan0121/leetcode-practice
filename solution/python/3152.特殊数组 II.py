class Solution:
    def isArraySpecial(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        bad_prefix = [0]
        for left, right in zip(nums, nums[1:]):
            bad_prefix.append(bad_prefix[-1] + int((left - right) % 2 == 0))
        return [bad_prefix[right] - bad_prefix[left] == 0 for left, right in queries]


if __name__ == "__main__":
    test_cases = [
        ([3, 4, 1, 2, 6], [[0, 4], [1, 3], [2, 4]], [False, True, False]),
    ]
    for _, (nums, queries, expected) in enumerate(test_cases):
        assert Solution().isArraySpecial(nums, queries) == expected
