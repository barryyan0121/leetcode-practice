from bisect import bisect_right


class Solution:
    def numberOfSubarrays(self, nums: list[int]) -> int:
        positions = {}
        decreasing = []
        answer = 0
        for index, value in enumerate(nums):
            while decreasing and nums[decreasing[-1]] <= value:
                decreasing.pop()
            previous_greater = decreasing[-1] if decreasing else -1
            positions.setdefault(value, []).append(index)
            answer += len(positions[value]) - bisect_right(
                positions[value], previous_greater
            )
            decreasing.append(index)
        return answer


if __name__ == "__main__":
    test_cases = [([1, 4, 3, 3, 2], 6), ([3, 3, 3], 6), ([2, 1, 2], 4)]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().numberOfSubarrays(nums) == expected
