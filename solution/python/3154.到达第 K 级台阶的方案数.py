from math import comb


class Solution:
    def waysToReachStair(self, k: int) -> int:
        mod = 10**9 + 7
        answer = 0
        jump = 0
        while (1 << jump) - (jump + 1) <= k:
            down = (1 << jump) - k
            if 0 <= down <= jump + 1:
                answer += comb(jump + 1, down)
            jump += 1
        return answer % mod


if __name__ == "__main__":
    test_cases = [(0, 2), (1, 4), (2, 4), (3, 3)]
    for _, (k, expected) in enumerate(test_cases):
        assert Solution().waysToReachStair(k) == expected
