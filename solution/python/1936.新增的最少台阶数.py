"""1936. 新增的最少台阶数"""


class Solution:
    def addRungs(self, rungs: list[int], dist: int) -> int:
        answer = 0
        previous = 0
        for rung in rungs:
            answer += (rung - previous - 1) // dist
            previous = rung
        return answer


if __name__ == "__main__":
    test_cases = [(([1, 3, 5, 10], 2), 2), (([3, 6, 8, 10], 3), 0)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().addRungs(*args) == expected
