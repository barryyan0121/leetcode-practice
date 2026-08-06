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
        if startPos[0] < homePos[0]:
            answer += sum(rowCosts[startPos[0] + 1 : homePos[0] + 1])
        else:
            answer += sum(rowCosts[homePos[0] : startPos[0]])
        if startPos[1] < homePos[1]:
            answer += sum(colCosts[startPos[1] + 1 : homePos[1] + 1])
        else:
            answer += sum(colCosts[homePos[1] : startPos[1]])
        return answer


if __name__ == "__main__":
    test_cases = [(([1, 0], [2, 3], [5, 4, 3], [8, 2, 6, 7]), 18)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minCost(*args) == expected
