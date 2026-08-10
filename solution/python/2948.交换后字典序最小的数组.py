"""2948. 交换后字典序最小的数组"""


class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        ordered = sorted((value, index) for index, value in enumerate(nums))
        answer = nums[:]
        start = 0
        while start < len(nums):
            end = start
            while (
                end + 1 < len(nums) and ordered[end + 1][0] - ordered[end][0] <= limit
            ):
                end += 1
            values = sorted(value for value, _ in ordered[start : end + 1])
            indices = sorted(index for _, index in ordered[start : end + 1])
            for index, value in zip(indices, values):
                answer[index] = value
            start = end + 1
        return answer


if __name__ == "__main__":
    assert Solution().lexicographicallySmallestArray([1, 5, 3, 9, 8], 2) == [
        1,
        3,
        5,
        8,
        9,
    ]
