class Solution:
    def earliestAcq(self, logs: list[list[int]], n: int) -> int:
        if n <= 1:
            return 0
        parent = list(range(n))
        components = n

        def find(person: int) -> int:
            while person != parent[person]:
                parent[person] = parent[parent[person]]
                person = parent[person]
            return person

        for timestamp, first, second in sorted(logs):
            first_root, second_root = find(first), find(second)
            if first_root != second_root:
                parent[first_root] = second_root
                components -= 1
                if components == 1:
                    return timestamp
        return -1


if __name__ == "__main__":
    test_cases = [
        (
            [
                [20190101, 0, 1],
                [20190104, 3, 4],
                [20190107, 2, 3],
                [20190211, 1, 5],
                [20190224, 2, 4],
                [20190301, 0, 3],
                [20190312, 1, 2],
                [20190322, 4, 5],
            ],
            6,
            20190301,
        ),
        ([[1, 0, 1], [2, 1, 2]], 4, -1),
        ([[1, 0, 1], [2, 0, 1], [3, 1, 2]], 3, 3),
        ([], 1, 0),
    ]
    for _, (logs, n, expected) in enumerate(test_cases):
        assert Solution().earliestAcq(logs, n) == expected
