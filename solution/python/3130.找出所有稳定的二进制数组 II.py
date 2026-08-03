class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        mod = 10**9 + 7
        end_zero = [[0] * (one + 1) for _ in range(zero + 1)]
        end_one = [[0] * (one + 1) for _ in range(zero + 1)]
        for count in range(1, min(one, limit) + 1):
            end_one[0][count] = 1

        zero_window = [0] * (one + 1)
        for count_zero in range(1, zero + 1):
            old_row = count_zero - limit - 1
            for count_one in range(one + 1):
                zero_window[count_one] += end_one[count_zero - 1][count_one]
                if old_row >= 0:
                    zero_window[count_one] -= end_one[old_row][count_one]
                zero_window[count_one] %= mod

            one_window = 0
            for count_one in range(one + 1):
                end_zero[count_zero][count_one] = (
                    1
                    if count_one == 0 and count_zero <= limit
                    else zero_window[count_one]
                )
                if count_one > 0:
                    one_window += end_zero[count_zero][count_one - 1]
                    if count_one - limit - 1 >= 0:
                        one_window -= end_zero[count_zero][count_one - limit - 1]
                    end_one[count_zero][count_one] = one_window % mod

        return (end_zero[zero][one] + end_one[zero][one]) % mod


if __name__ == "__main__":
    test_cases = [(1, 1, 2, 2), (1, 2, 1, 1), (3, 3, 2, 14)]
    for _, (zero, one, limit, expected) in enumerate(test_cases):
        assert Solution().numberOfStableArrays(zero, one, limit) == expected
