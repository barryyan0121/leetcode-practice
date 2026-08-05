"""2523. 范围内最接近的两个质数"""


class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        prime = [True] * (right + 1)
        prime[:2] = [False, False]
        for value in range(2, int(right**0.5) + 1):
            if prime[value]:
                prime[value * value : right + 1 : value] = [False] * (
                    (right - value * value) // value + 1
                )
        candidates = [value for value in range(left, right + 1) if prime[value]]
        if len(candidates) < 2:
            return [-1, -1]
        pair = min(
            zip(candidates, candidates[1:]), key=lambda values: values[1] - values[0]
        )
        return list(pair)


if __name__ == "__main__":
    test_cases = [((10, 19), [11, 13])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().closestPrimes(*args) == expected
