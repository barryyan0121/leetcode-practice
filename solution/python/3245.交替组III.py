from bisect import bisect_left


class Fenwick:
    def __init__(self, size: int):
        self.tree = [0] * (size + 1)

    def add(self, index: int, value: int) -> None:
        index += 1
        while index < len(self.tree):
            self.tree[index] += value
            index += index & -index

    def prefix(self, index: int) -> int:
        result = 0
        index += 1
        while index:
            result += self.tree[index]
            index -= index & -index
        return result


class Solution:
    def numberOfAlternatingGroups(
        self, colors: list[int], queries: list[list[int]]
    ) -> list[int]:
        n = len(colors)
        bad = [int(colors[index] == colors[(index + 1) % n]) for index in range(n)]
        size = 1
        while size < n:
            size *= 2
        segment = [0] * (2 * size)
        for index, value in enumerate(bad):
            segment[size + index] = value
        for index in range(size - 1, 0, -1):
            segment[index] = segment[2 * index] + segment[2 * index + 1]

        def set_bad(index: int, value: int) -> None:
            if bad[index] == value:
                return
            bad[index] = value
            node = size + index
            segment[node] = value
            node //= 2
            while node:
                segment[node] = segment[2 * node] + segment[2 * node + 1]
                node //= 2

        def first(start: int) -> int:
            def search(node: int, left: int, right: int) -> int:
                if right <= start or segment[node] == 0:
                    return -1
                if right - left == 1:
                    return left if left < n else -1
                middle = (left + right) // 2
                result = search(2 * node, left, middle)
                return result if result != -1 else search(2 * node + 1, middle, right)

            return search(1, 0, size)

        def last(end: int) -> int:
            def search(node: int, left: int, right: int) -> int:
                if left > end or segment[node] == 0:
                    return -1
                if right - left == 1:
                    return left if left < n else -1
                middle = (left + right) // 2
                result = search(2 * node + 1, middle, right)
                return result if result != -1 else search(2 * node, left, middle)

            return search(1, 0, size)

        gap_count = Fenwick(n + 1)
        gap_sum = Fenwick(n + 1)
        bad_total = sum(bad)

        def gap(left: int, right: int) -> int:
            return (right - left) % n or n

        def change_gap(length: int, delta: int) -> None:
            gap_count.add(length, delta)
            gap_sum.add(length, delta * length)

        if bad_total:
            positions = [index for index, value in enumerate(bad) if value]
            for index, position in enumerate(positions):
                change_gap(gap(position, positions[(index + 1) % len(positions)]), 1)

        def insert_bad(position: int) -> None:
            nonlocal bad_total
            if bad_total == 0:
                change_gap(n, 1)
            else:
                previous = last(position - 1)
                following = first(position + 1)
                if previous == -1:
                    previous = last(n - 1)
                if following == -1:
                    following = first(0)
                change_gap(gap(previous, following), -1)
                change_gap(gap(previous, position), 1)
                change_gap(gap(position, following), 1)
            set_bad(position, 1)
            bad_total += 1

        def remove_bad(position: int) -> None:
            nonlocal bad_total
            if bad_total == 1:
                change_gap(n, -1)
            else:
                previous = last(position - 1)
                following = first(position + 1)
                if previous == -1:
                    previous = last(n - 1)
                if following == -1:
                    following = first(0)
                change_gap(gap(previous, position), -1)
                change_gap(gap(position, following), -1)
                change_gap(gap(previous, following), 1)
            set_bad(position, 0)
            bad_total -= 1

        answer = []
        for query in queries:
            if query[0] == 1:
                size_needed = query[1]
                if not bad_total:
                    answer.append(n)
                else:
                    threshold = size_needed - 1
                    total_count = gap_count.prefix(n)
                    total_sum = gap_sum.prefix(n)
                    small_count = gap_count.prefix(threshold)
                    small_sum = gap_sum.prefix(threshold)
                    answer.append(
                        total_sum - small_sum - threshold * (total_count - small_count)
                    )
            else:
                index, color = query[1], query[2]
                if colors[index] != color:
                    for edge in {(index - 1) % n, index}:
                        if bad[edge]:
                            remove_bad(edge)
                    colors[index] = color
                    for edge in {(index - 1) % n, index}:
                        if colors[edge] == colors[(edge + 1) % n]:
                            insert_bad(edge)
        return answer


if __name__ == "__main__":
    test_cases = [
        (([0, 1, 1, 0, 1], [[2, 1, 0], [1, 4]]), [2]),
        (([0, 0, 1, 0, 1, 1], [[1, 3], [2, 3, 0], [1, 5]]), [2, 0]),
    ]
    for _, ((colors, queries), expected) in enumerate(test_cases):
        assert Solution().numberOfAlternatingGroups(colors, queries) == expected
