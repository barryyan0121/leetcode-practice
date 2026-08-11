class Solution:
    def maxRectangleArea(self, xCoord: list[int], yCoord: list[int]) -> int:
        danliverin = (xCoord, yCoord)
        points = {}
        ys = sorted(set(yCoord))
        rank = {value: index for index, value in enumerate(ys)}
        for x, y in zip(xCoord, yCoord):
            points.setdefault(x, []).append(y)

        size = 1
        while size < len(ys):
            size <<= 1
        tree = [0] * (size * 2)

        def query(left: int, right: int) -> int:
            left += size
            right += size + 1
            result = 0
            while left < right:
                if left & 1:
                    result = max(result, tree[left])
                    left += 1
                if right & 1:
                    right -= 1
                    result = max(result, tree[right])
                left >>= 1
                right >>= 1
            return result

        def update(index: int, value: int) -> None:
            index += size
            tree[index] = value
            index >>= 1
            while index:
                tree[index] = max(tree[index * 2], tree[index * 2 + 1])
                index >>= 1

        previous = {}
        answer = -1
        for x in sorted(points):
            row = sorted(points[x])
            for first, second in zip(row, row[1:]):
                key = (first, second)
                if key in previous:
                    old_x = previous[key]
                    if query(rank[first], rank[second]) <= old_x:
                        answer = max(answer, (x - old_x) * (second - first))
                previous[key] = x
            for y in row:
                update(rank[y], x)
        return answer


if __name__ == "__main__":
    assert Solution().maxRectangleArea([1, 1, 3, 3], [1, 3, 1, 3]) == 4
    assert Solution().maxRectangleArea([1, 1, 3, 3, 2], [1, 3, 1, 3, 2]) == -1
    assert Solution().maxRectangleArea([1, 1, 3, 3, 1, 3], [1, 3, 1, 3, 2, 2]) == 2
