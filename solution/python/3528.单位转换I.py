"""3528. 单位转换 I"""


class Solution:
    def baseUnitConversions(self, conversions: list[list[int]]) -> list[int]:
        n = len(conversions) + 1
        graph = [[] for _ in range(n)]
        for source, target, factor in conversions:
            graph[source].append((target, factor))

        modulo = 10**9 + 7
        answer = [0] * n
        answer[0] = 1
        stack = [0]
        while stack:
            source = stack.pop()
            for target, factor in graph[source]:
                answer[target] = answer[source] * factor % modulo
                stack.append(target)
        return answer


if __name__ == "__main__":
    test_cases = [
        (([[0, 1, 2], [1, 2, 3]],), [1, 2, 6]),
        (
            (
                [
                    [0, 1, 2],
                    [0, 2, 3],
                    [1, 3, 4],
                    [1, 4, 5],
                    [2, 5, 2],
                    [4, 6, 3],
                    [5, 7, 4],
                ],
            ),
            [1, 2, 3, 8, 10, 6, 30, 24],
        ),
    ]
    for _, ((conversions,), expected) in enumerate(test_cases):
        assert Solution().baseUnitConversions(conversions) == expected
