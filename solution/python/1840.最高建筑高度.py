"""1840. 最高建筑高度"""


class Solution:
    def maxBuilding(self, n: int, restrictions: list[list[int]]) -> int:
        limits = [[1, 0], *restrictions, [n, n - 1]]
        limits.sort()
        for index in range(1, len(limits)):
            distance = limits[index][0] - limits[index - 1][0]
            limits[index][1] = min(limits[index][1], limits[index - 1][1] + distance)
        for index in range(len(limits) - 2, -1, -1):
            distance = limits[index + 1][0] - limits[index][0]
            limits[index][1] = min(limits[index][1], limits[index + 1][1] + distance)
        answer = 0
        for (left, left_height), (right, right_height) in zip(limits, limits[1:]):
            answer = max(answer, (left_height + right_height + right - left) // 2)
        return answer


if __name__ == "__main__":
    test_cases = [((5, [[2, 1], [4, 1]]), 2), ((6, []), 5)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maxBuilding(*args) == expected
