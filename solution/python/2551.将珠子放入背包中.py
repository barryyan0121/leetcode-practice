# @lc app=leetcode.cn id=2551 lang=python3


class Solution:
    def putMarbles(self, weights: list[int], k: int) -> int:
        pair_sums = sorted(
            weights[index] + weights[index + 1] for index in range(len(weights) - 1)
        )
        return sum(pair_sums[-k + 1 :]) - sum(pair_sums[: k - 1])


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.putMarbles, ([1, 3, 5, 1], 2), 4),
        (solution.putMarbles, ([1, 3], 2), 0),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 2551 题 "将珠子放入背包中" 所有测试用例通过')
