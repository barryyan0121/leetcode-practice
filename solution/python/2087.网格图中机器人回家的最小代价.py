"""2087. 网格图中机器人回家的最小代价"""


class Solution:
    def minCost(
        self,
        startPos: list[int],
        homePos: list[int],
        rowCosts: list[int],
        colCosts: list[int],
    ) -> int:
        answer = 0
        for row in range(min(startPos[0], homePos[0]), max(startPos[0], homePos[0])):
            answer += rowCosts[row + (startPos[0] > homePos[0])]
        for col in range(min(startPos[1], homePos[1]), max(startPos[1], homePos[1])):
            answer += colCosts[col + (startPos[1] > homePos[1])]
        return answer


if __name__ == "__main__":
    test_cases = [(([1, 0], [2, 3], [5, 4, 3], [8, 2, 6, 7]), 18)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minCost(*args) == expected
