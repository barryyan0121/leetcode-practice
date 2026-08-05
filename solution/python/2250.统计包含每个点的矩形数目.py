"""2250. 统计包含每个点的矩形数目"""

from bisect import bisect_left


class Solution:
    def countRectangles(
        self, rectangles: list[list[int]], points: list[list[int]]
    ) -> list[int]:
        heights = sorted({height for _, height in rectangles})
        bit = [0] * (len(heights) + 1)

        def add(index: int) -> None:
            while index < len(bit):
                bit[index] += 1
                index += index & -index

        def suffix(index: int) -> int:
            index = len(heights) - index
            total = 0
            while index:
                total += bit[index]
                index -= index & -index
            return total

        rectangles.sort(reverse=True)
        order = sorted(range(len(points)), key=lambda i: points[i][0], reverse=True)
        answer = [0] * len(points)
        position = 0
        for point_index in order:
            x, y = points[point_index]
            while position < len(rectangles) and rectangles[position][0] >= x:
                add(len(heights) - bisect_left(heights, rectangles[position][1]))
                position += 1
            answer[point_index] = suffix(bisect_left(heights, y))
        return answer


if __name__ == "__main__":
    test_cases = [(([[1, 2], [2, 3], [2, 5]], [[2, 1], [1, 4]]), [2, 1])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().countRectangles(*args) == expected
