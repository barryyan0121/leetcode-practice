"""1943. 描述绘画结果"""


class Solution:
    def splitPainting(self, segments: list[list[int]]) -> list[list[int]]:
        changes = {}
        for start, end, color in segments:
            changes[start] = changes.get(start, 0) + color
            changes[end] = changes.get(end, 0) - color
        answer = []
        previous = None
        color = 0
        for point in sorted(changes):
            if previous is not None and color:
                answer.append([previous, point, color])
            color += changes[point]
            previous = point
        return answer


if __name__ == "__main__":
    test_cases = [(([[1, 4, 5], [4, 7, 7], [1, 7, 9]],), [[1, 4, 14], [4, 7, 16]])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().splitPainting(*args) == expected
