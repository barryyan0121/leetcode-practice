"""2067. 等计数子串"""


class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        distance = abs(endPos - startPos)
        if distance > k or (k - distance) % 2:
            return 0
        steps = (k + distance) // 2
        answer = 1
        modulus = 10**9 + 7
        for index in range(1, steps + 1):
            answer = answer * (k - steps + index) * pow(index, -1, modulus) % modulus
        return answer


if __name__ == "__main__":
    test_cases = [((1, 2, 3), 3), ((2, 5, 10), 0)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().numberOfWays(*args) == expected
