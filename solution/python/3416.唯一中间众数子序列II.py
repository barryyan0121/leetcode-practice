from collections import Counter
from math import comb


class Solution:
    def subsequencesWithMiddleMode(self, nums: list[int]) -> int:
        felorintho = nums
        mod = 10**9 + 7
        n = len(nums)
        left = Counter(nums[:2])
        right = Counter(nums[2:])
        left_size, right_size = 2, n - 2
        c2 = lambda value: value * (value - 1) // 2
        pair_left = sum(c2(value) for value in left.values())
        pair_right = sum(c2(value) for value in right.values())
        sum_lr = sum(left[value] * right[value] for value in left.keys() | right.keys())
        sum_lr2 = sum(
            left[value] * right[value] ** 2 for value in left.keys() | right.keys()
        )
        sum_l2r = sum(
            left[value] ** 2 * right[value] for value in left.keys() | right.keys()
        )

        def change_left(value: int, delta: int) -> None:
            nonlocal pair_left, sum_lr, sum_lr2, sum_l2r
            old = left[value]
            other = right[value]
            pair_left += old if delta > 0 else -(old - 1)
            sum_lr += delta * other
            sum_lr2 += delta * other * other
            sum_l2r += ((old + delta) ** 2 - old**2) * other
            left[value] = old + delta

        def change_right(value: int, delta: int) -> None:
            nonlocal pair_right, sum_lr, sum_lr2, sum_l2r
            old = right[value]
            other = left[value]
            pair_right += old if delta > 0 else -(old - 1)
            sum_lr += delta * other
            sum_l2r += delta * other * other
            sum_lr2 += ((old + delta) ** 2 - old**2) * other
            right[value] = old + delta

        answer = 0
        for middle in range(2, n - 2):
            value = nums[middle]
            change_right(value, -1)
            right_size -= 1
            left_value, right_value = left[value], right[value]
            left_other, right_other = left_size - left_value, right_size - right_value
            total = c2(left_size) * c2(right_size)
            zero = c2(left_other) * c2(right_other)
            one = (
                left_value * left_other * c2(right_other)
                + c2(left_other) * right_value * right_other
            )
            lr = sum_lr - left_value * right_value
            lr2 = sum_lr2 - left_value * right_value**2
            l2r = sum_l2r - left_value**2 * right_value
            distinct_left_right = (
                left_other * c2(right_other)
                - left_other * (pair_right - c2(right_value))
                - (right_other * lr - lr2)
            )
            distinct_right_left = (
                right_other * c2(left_other)
                - right_other * (pair_left - c2(left_value))
                - (left_other * lr - l2r)
            )
            answer += total - zero - one
            answer += (
                left_value * distinct_left_right + right_value * distinct_right_left
            )
            change_left(value, 1)
            left_size += 1
        return answer % mod


if __name__ == "__main__":
    assert Solution().subsequencesWithMiddleMode([1, 1, 1, 1, 1, 1]) == 6
    assert Solution().subsequencesWithMiddleMode([1, 2, 2, 3, 3, 4]) == 4
    assert Solution().subsequencesWithMiddleMode(list(range(9))) == 0
