"""2139. 得到目标分数的最少移动次数"""


class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        answer = 0
        while target > 1 and maxDoubles:
            answer += target % 2
            target //= 2
            maxDoubles -= 1
            answer += 1
        return answer + target - 1


if __name__ == "__main__":
    test_cases = [((5, 0), 4), ((10, 4), 4)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minMoves(*args) == expected
