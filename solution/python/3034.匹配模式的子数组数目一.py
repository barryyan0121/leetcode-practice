"""3034. 匹配模式的子数组数目 I"""


class Solution:
    def countMatchingSubarrays(self, nums: list[int], pattern: list[int]) -> int:
        relation = [
            1 if left < right else -1 if left > right else 0
            for left, right in zip(nums, nums[1:])
        ]
        size = len(pattern)
        return sum(
            relation[index : index + size] == pattern
            for index in range(len(relation) - size + 1)
        )


if __name__ == "__main__":
    assert Solution().countMatchingSubarrays([1, 2, 3, 4, 5], [1, 1]) == 3
