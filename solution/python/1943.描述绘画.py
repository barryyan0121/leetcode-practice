"""1943. 描述绘画"""


class Solution:
    def splitPainting(self, segments: list[list[int]]) -> list[list[int]]:
        changes = {}
        for left, right, color in segments:
            changes[left] = changes.get(left, 0) + color
            changes[right] = changes.get(right, 0) - color
        points = sorted(changes)
        result = []
        current = 0
        for left, right in zip(points, points[1:]):
            current += changes[left]
            if current:
                result.append([left, right, current])
        return result


if __name__ == "__main__":
    assert Solution().splitPainting([[1, 4, 5], [4, 7, 7], [1, 7, 9]]) == [
        [1, 4, 14],
        [4, 7, 16],
    ]
