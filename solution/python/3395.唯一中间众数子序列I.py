from collections import Counter
from math import comb


class Solution:
    def subsequencesWithMiddleMode(self, nums: list[int]) -> int:
        felorintho = nums
        mod = 10**9 + 7
        n = len(nums)
        right = Counter(nums[2:])
        left = Counter(nums[:2])
        answer = 0

        def distinct(left_count, right_count, excluded):
            dp = [[0] * 3 for _ in range(3)]
            dp[0][0] = 1
            for value in set(left) | set(right):
                if value == excluded:
                    continue
                next_dp = [[0] * 3 for _ in range(3)]
                l_count, r_count = left[value], right[value]
                for used_left in range(3):
                    for used_right in range(3):
                        base = dp[used_left][used_right]
                        if not base:
                            continue
                        for take_left in range(min(1, 2 - used_left, l_count) + 1):
                            for take_right in range(
                                min(1, 2 - used_right, r_count) + 1
                            ):
                                if take_left and take_right:
                                    continue
                                next_dp[used_left + take_left][
                                    used_right + take_right
                                ] += (
                                    base
                                    * comb(l_count, take_left)
                                    * comb(r_count, take_right)
                                )
                dp = next_dp
            return dp[left_count][right_count]

        for middle in range(2, n - 2):
            value = nums[middle]
            right[value] -= 1
            left_size, right_size = middle, n - middle - 1
            left_value = left[value]
            right_value = right[value]
            total = comb(left_size, 2) * comb(right_size, 2)
            zero_x = comb(left_size - left_value, 2) * comb(right_size - right_value, 2)
            one_x = left_value * (left_size - left_value) * comb(
                right_size - right_value, 2
            ) + comb(left_size - left_value, 2) * right_value * (
                right_size - right_value
            )
            answer += total - zero_x - one_x
            answer += left_value * distinct(1, 2, value)
            answer += right_value * distinct(2, 1, value)
            left[value] += 1
        return answer % mod


if __name__ == "__main__":
    assert Solution().subsequencesWithMiddleMode([1, 1, 1, 1, 1, 1]) == 6
    assert Solution().subsequencesWithMiddleMode([1, 2, 2, 3, 3, 4]) == 4
    assert Solution().subsequencesWithMiddleMode(list(range(9))) == 0
