class Solution:
    def leftmostBuildingQueries(
        self, heights: list[int], queries: list[list[int]]
    ) -> list[int]:
        answer = []
        for a, b in queries:
            if a > b:
                a, b = b, a
            if a == b or heights[a] < heights[b]:
                answer.append(b)
                continue
            index = b + 1
            while index < len(heights) and heights[index] <= heights[a]:
                index += 1
            answer.append(index if index < len(heights) else -1)
        return answer


assert Solution().leftmostBuildingQueries(
    [6, 4, 8, 5, 2, 7], [[0, 1], [0, 3], [2, 4], [3, 4], [2, 2]]
) == [2, 5, -1, 5, 2]
