"""2826. 将三个组排序"""


class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        keep = [0, 0, 0]
        for value in nums:
            keep[value - 1] += 1
            keep[1] = max(keep[1], keep[0])
            keep[2] = max(keep[2], keep[1])
        return len(nums) - keep[2]


if __name__ == "__main__":
    assert Solution().minimumOperations([2, 1, 3, 2, 1]) == 3
