class Solution:
    def maxPathLength(self, coordinates: list[list[int]], k: int) -> int:
        n = len(coordinates)
        ys = sorted({point[1] for point in coordinates})
        ranks = {value: index + 1 for index, value in enumerate(ys)}

        def longest(order: list[int], reverse_y: bool) -> list[int]:
            tree = [0] * (n + 1)

            def query(index: int) -> int:
                result = 0
                while index:
                    result = max(result, tree[index])
                    index -= index & -index
                return result

            def update(index: int, value: int) -> None:
                while index <= n:
                    tree[index] = max(tree[index], value)
                    index += index & -index

            result = [1] * n
            position = 0
            while position < n:
                end = position
                x = coordinates[order[position]][0]
                while end < n and coordinates[order[end]][0] == x:
                    end += 1
                pending = []
                for index in order[position:end]:
                    rank = ranks[coordinates[index][1]]
                    if reverse_y:
                        rank = len(ys) - rank + 1
                    result[index] = query(rank - 1) + 1
                    pending.append((rank, result[index]))
                for rank, value in pending:
                    update(rank, value)
                position = end
            return result

        ascending = sorted(range(n), key=lambda index: coordinates[index][0])
        descending = sorted(range(n), key=lambda index: -coordinates[index][0])
        left = longest(ascending, False)
        right = longest(descending, True)
        return left[k] + right[k] - 1


if __name__ == "__main__":
    test_cases = [
        (([[3, 1], [2, 2], [4, 1], [0, 0], [5, 3]], 1), 3),
        (([[2, 1], [7, 0], [5, 6]], 2), 2),
    ]
    for _, ((coordinates, k), expected) in enumerate(test_cases):
        assert Solution().maxPathLength(coordinates, k) == expected
