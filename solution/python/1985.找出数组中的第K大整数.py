"""1985. 找出数组中的第 K 大整数"""


class Solution:
    def kthLargestNumber(self, nums: list[str], k: int) -> str:
        return sorted(nums, key=lambda value: (len(value), value), reverse=True)[k - 1]


if __name__ == "__main__":
    test_cases = [((["3", "6", "7", "10"], 4), "3")]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().kthLargestNumber(*args) == expected
