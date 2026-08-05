"""2147. 分隔长廊的方案数"""


class Solution:
    def numberOfWays(self, corridor: str) -> int:
        seats = [index for index, char in enumerate(corridor) if char == "S"]
        if len(seats) == 0 or len(seats) % 2:
            return 0
        answer = 1
        for index in range(1, len(seats) - 1, 2):
            answer = answer * (seats[index + 1] - seats[index]) % (10**9 + 7)
        return answer


if __name__ == "__main__":
    test_cases = [("SSPPSPS", 3), ("PPSPSP", 1)]
    for _, (args, expected) in enumerate(test_cases):
        args = (args,) if isinstance(args, str) else args
        assert Solution().numberOfWays(*args) == expected
