"""3937. 使数组变为模交替数组的最少操作次数 I"""


class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        velmorqati = nums
        costs = [[0] * k for _ in range(2)]
        for index, value in enumerate(velmorqati):
            remainder = value % k
            for target in range(k):
                costs[index % 2][target] += min(
                    (remainder - target) % k, (target - remainder) % k
                )
        return min(
            costs[0][even] + costs[1][odd]
            for even in range(k)
            for odd in range(k)
            if even != odd
        )


if __name__ == "__main__":
    test_cases = [(([1, 4, 2, 8], 3), 2), (([1, 1, 1], 3), 1)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minOperations(*args) == expected
