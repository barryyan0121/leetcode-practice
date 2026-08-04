from functools import cmp_to_key


class Solution:
    def maxGoodNumber(self, nums: list[int]) -> int:
        bits = [bin(number)[2:] for number in nums]

        def compare(first: str, second: str) -> int:
            return -1 if first + second > second + first else 1

        bits.sort(key=cmp_to_key(compare))
        return int("".join(bits), 2)


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 3],), 30),
        (([2, 8, 16],), 1296),
    ]
    for _, ((nums,), expected) in enumerate(test_cases):
        assert Solution().maxGoodNumber(nums) == expected
