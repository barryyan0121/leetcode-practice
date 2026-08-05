"""3577. 统计计算机解锁顺序排列数"""


class Solution:
    def countPermutations(self, complexity: list[int]) -> int:
        if any(value <= complexity[0] for value in complexity[1:]):
            return 0
        answer = 1
        for value in range(2, len(complexity)):
            answer = answer * value % (10**9 + 7)
        return answer


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 3],), 2),
        (([3, 3, 3, 4, 4, 4],), 0),
    ]
    for _, ((complexity,), expected) in enumerate(test_cases):
        assert Solution().countPermutations(complexity) == expected
