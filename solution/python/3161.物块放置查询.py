from bisect import bisect_left


class Fenwick:
    def __init__(self, size: int):
        self.tree = [0] * (size + 1)

    def add(self, index: int, value: int) -> None:
        index += 1
        while index < len(self.tree):
            self.tree[index] += value
            index += index & -index

    def sum(self, count: int) -> int:
        result = 0
        while count:
            result += self.tree[count]
            count -= count & -count
        return result

    def kth(self, order: int) -> int:
        index = 0
        bit = 1 << (len(self.tree).bit_length() - 1)
        while bit:
            candidate = index + bit
            if candidate < len(self.tree) and self.tree[candidate] < order:
                index = candidate
                order -= self.tree[candidate]
            bit >>= 1
        return index


class SegmentTree:
    def __init__(self, size: int):
        self.base = 1
        while self.base < size:
            self.base <<= 1
        self.tree = [0] * (2 * self.base)

    def update(self, index: int, value: int) -> None:
        index += self.base
        self.tree[index] = value
        index >>= 1
        while index:
            self.tree[index] = max(self.tree[index * 2], self.tree[index * 2 + 1])
            index >>= 1

    def query(self, right: int) -> int:
        left = self.base
        right += self.base + 1
        result = 0
        while left < right:
            if left & 1:
                result = max(result, self.tree[left])
                left += 1
            if right & 1:
                right -= 1
                result = max(result, self.tree[right])
            left >>= 1
            right >>= 1
        return result


class Solution:
    def getResults(self, queries: list[list[int]]) -> list[bool]:
        coordinates = sorted({0, *(query[1] for query in queries)})
        index_of = {value: index for index, value in enumerate(coordinates)}
        fenwick = Fenwick(len(coordinates))
        segments = SegmentTree(len(coordinates))
        zero_index = index_of[0]
        fenwick.add(zero_index, 1)
        segments.update(zero_index, 0)
        answer = []

        for query in queries:
            position = query[1]
            index = index_of[position]
            if query[0] == 1:
                before = fenwick.sum(index)
                previous = fenwick.kth(before) if before else None
                through = fenwick.sum(index + 1)
                total = fenwick.sum(len(coordinates))
                following = fenwick.kth(through + 1) if through < total else None
                if following is not None:
                    segments.update(following, coordinates[following] - position)
                segments.update(index, position - coordinates[previous])
                fenwick.add(index, 1)
            else:
                before = fenwick.sum(index + 1)
                previous = fenwick.kth(before)
                longest = max(segments.query(index), position - coordinates[previous])
                answer.append(longest >= query[2])
        return answer


if __name__ == "__main__":
    test_cases = [
        (
            [[1, 3], [2, 5, 3], [2, 5, 4], [2, 3, 3]],
            [True, False, True],
        )
    ]
    for _, (queries, expected) in enumerate(test_cases):
        assert Solution().getResults(queries) == expected
