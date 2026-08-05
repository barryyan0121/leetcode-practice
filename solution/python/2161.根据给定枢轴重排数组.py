"""2161. 根据给定枢轴重排数组"""


class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        return (
            [x for x in nums if x < pivot]
            + [x for x in nums if x == pivot]
            + [x for x in nums if x > pivot]
        )


if __name__ == "__main__":
    test_cases = [(([9, 12, 5, 10, 14, 3, 10], 10), [9, 5, 3, 10, 10, 12, 14])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().pivotArray(*args) == expected
