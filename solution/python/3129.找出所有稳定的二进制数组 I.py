class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        mod = 10**9 + 7
        end_zero = [[0] * (one + 1) for _ in range(zero + 1)]
        end_one = [[0] * (one + 1) for _ in range(zero + 1)]
        for count in range(1, min(zero, limit) + 1):
            end_zero[count][0] = 1
        for count in range(1, min(one, limit) + 1):
            end_one[0][count] = 1

        for count_zero in range(1, zero + 1):
            for count_one in range(1, one + 1):
                end_zero[count_zero][count_one] = (
                    sum(
                        end_one[count_zero - run][count_one]
                        for run in range(1, min(limit, count_zero) + 1)
                    )
                    % mod
                )
                end_one[count_zero][count_one] = (
                    sum(
                        end_zero[count_zero][count_one - run]
                        for run in range(1, min(limit, count_one) + 1)
                    )
                    % mod
                )
        return (end_zero[zero][one] + end_one[zero][one]) % mod


if __name__ == "__main__":
    test_cases = [(1, 1, 2, 2), (1, 2, 1, 1), (3, 3, 2, 14)]
    for _, (zero, one, limit, expected) in enumerate(test_cases):
        assert Solution().numberOfStableArrays(zero, one, limit) == expected
