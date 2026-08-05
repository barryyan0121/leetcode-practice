"""2442. 反转之后不同整数的数目"""


class Solution:
    def countDistinctIntegers(self, nums: list[int]) -> int:
        values = set(nums)
        values.update(int(str(value)[::-1]) for value in nums)
        return len(values)


if __name__ == "__main__":
    test_cases = [(([1, 13, 10, 12, 31],), 6)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().countDistinctIntegers(*args) == expected
