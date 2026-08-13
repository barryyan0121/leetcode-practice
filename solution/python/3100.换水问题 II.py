"""3100. 换水问题 II"""


class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        answer = numBottles
        empty = numBottles
        while empty >= numExchange:
            empty -= numExchange
            answer += 1
            empty += 1
            numExchange += 1
        return answer


if __name__ == "__main__":
    test_cases = [((13, 6), 15), ((10, 3), 13)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maxBottlesDrunk(*args) == expected
