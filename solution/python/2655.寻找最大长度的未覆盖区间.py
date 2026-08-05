"""2655. 寻找最大长度的未覆盖区间"""


class Solution:
    def findMaximalUncoveredRanges(
        self, n: int, ranges: list[list[int]]
    ) -> list[list[int]]:
        answer = []
        covered_end = 0
        for start, end in sorted(ranges):
            if start > covered_end:
                answer.append([covered_end, start - 1])
            covered_end = max(covered_end, end + 1)
        if covered_end < n:
            answer.append([covered_end, n - 1])
        return answer


if __name__ == "__main__":
    test_cases = [((10, [[3, 5], [7, 8]]), [[0, 2], [6, 6], [9, 9]])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().findMaximalUncoveredRanges(*args) == expected
