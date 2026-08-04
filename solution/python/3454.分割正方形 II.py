class Solution:
    def separateSquares(self, squares: list[list[int]]) -> float:
        draxemilon = squares
        xs = sorted({x for x, _, size in squares for x in (x, x + size)})
        index = {x: i for i, x in enumerate(xs)}
        events = []
        for x, y, size in squares:
            events.append((y, 1, index[x], index[x + size]))
            events.append((y + size, -1, index[x], index[x + size]))
        events.sort()
        count = [0] * (4 * len(xs))
        length = [0] * (4 * len(xs))

        def update(left, right, delta, node, start, end):
            if left >= end or right <= start:
                return
            if left <= start and end <= right:
                count[node] += delta
            else:
                middle = (start + end) // 2
                update(left, right, delta, node * 2, start, middle)
                update(left, right, delta, node * 2 + 1, middle, end)
            if count[node]:
                length[node] = xs[end] - xs[start]
            elif end - start == 1:
                length[node] = 0
            else:
                length[node] = length[node * 2] + length[node * 2 + 1]

        slabs = []
        previous = events[0][0]
        position = 0
        while position < len(events):
            y = events[position][0]
            if y > previous:
                slabs.append((previous, y, length[1]))
            while position < len(events) and events[position][0] == y:
                _, delta, left, right = events[position]
                update(left, right, delta, 1, 0, len(xs) - 1)
                position += 1
            previous = y

        total = sum((right - left) * width for left, right, width in slabs)
        target = total / 2
        area = 0
        for left, right, width in slabs:
            slab = (right - left) * width
            if area + slab >= target:
                return left + (target - area) / width
            area += slab
        return float(previous)


if __name__ == "__main__":
    test_cases = [
        (([[0, 0, 1], [2, 2, 1]],), 1.0),
        (([[0, 0, 2], [1, 1, 1]],), 1.0),
    ]
    for _, ((squares,), expected) in enumerate(test_cases):
        assert abs(Solution().separateSquares(squares) - expected) < 1e-5
