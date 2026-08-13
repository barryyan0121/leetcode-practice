"""3914. 使数组非递减需要的最小累计值"""


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        dravonikel = nums
        return sum(
            max(0, dravonikel[index - 1] - dravonikel[index])
            for index in range(1, len(dravonikel))
        )


if __name__ == "__main__":
    test_cases = [
        (([3, 1, 2],), 2),
        (([1, 2, 3],), 0),
        (([5, 1, 1],), 4),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minOperations(*args) == expected
