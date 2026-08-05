"""2672. 有相同颜色的相邻元素数目"""


class Solution:
    def colorTheArray(self, n: int, queries: list[list[int]]) -> list[int]:
        colors = [0] * n
        answer = 0
        result = []
        for index, color in queries:
            if colors[index] and index and colors[index - 1] == colors[index]:
                answer -= 1
            if colors[index] and index + 1 < n and colors[index + 1] == colors[index]:
                answer -= 1
            colors[index] = color
            if index and colors[index - 1] == color:
                answer += 1
            if index + 1 < n and colors[index + 1] == color:
                answer += 1
            result.append(answer)
        return result


if __name__ == "__main__":
    test_cases = [((4, [[0, 2], [1, 2], [3, 1], [1, 1], [2, 1]]), [0, 1, 1, 0, 2])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().colorTheArray(*args) == expected
