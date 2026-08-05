"""3595. 一次或两次"""


class Solution:
    def onceTwice(self, nums: list[int]) -> list[int]:
        mask = (1 << 32) - 1
        all_ones = all_twos = 0
        for value in nums:
            value &= mask
            all_ones = (all_ones ^ value) & ~all_twos & mask
            all_twos = (all_twos ^ value) & ~all_ones & mask

        diff_bit = (all_ones ^ all_twos) & -(all_ones ^ all_twos)
        ones = twos = group_size = 0
        other_ones = other_twos = other_size = 0
        for value in nums:
            if value & diff_bit:
                group_size += 1
                ones = (ones ^ value) & ~twos & mask
                twos = (twos ^ value) & ~ones & mask
            else:
                other_size += 1
                other_ones = (other_ones ^ value) & ~other_twos & mask
                other_twos = (other_twos ^ value) & ~other_ones & mask

        special = ones if group_size % 3 == 1 else twos
        other = other_ones if other_size % 3 == 1 else other_twos

        def signed(value):
            return value if value < 1 << 31 else value - (1 << 32)

        result = [special, other] if group_size % 3 == 1 else [other, special]
        return [signed(value) for value in result]


if __name__ == "__main__":
    test_cases = [
        (([2, 2, 3, 2, 5, 5, 5, 7, 7],), [3, 7]),
        (([4, 4, 6, 4, 9, 9, 9, 6, 8],), [8, 6]),
        (([0, 0, 1, 2, 2, 2],), [1, 0]),
    ]
    for _, ((nums,), expected) in enumerate(test_cases):
        assert Solution().onceTwice(nums) == expected
