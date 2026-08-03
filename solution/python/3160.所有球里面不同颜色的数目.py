from collections import Counter


class Solution:
    def queryResults(self, limit: int, queries: list[list[int]]) -> list[int]:
        ball_color = {}
        colors = Counter()
        answer = []
        for ball, color in queries:
            if ball in ball_color:
                old_color = ball_color[ball]
                colors[old_color] -= 1
                if colors[old_color] == 0:
                    del colors[old_color]
            ball_color[ball] = color
            colors[color] += 1
            answer.append(len(colors))
        return answer


if __name__ == "__main__":
    test_cases = [(4, [[1, 4], [2, 5], [1, 3], [3, 4]], [1, 2, 2, 3])]
    for _, (limit, queries, expected) in enumerate(test_cases):
        assert Solution().queryResults(limit, queries) == expected
