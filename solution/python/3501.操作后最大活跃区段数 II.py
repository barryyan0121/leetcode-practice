from bisect import bisect_left, bisect_right
from re import finditer


class Solution:
    def maxActiveSectionsAfterTrade(
        self, s: str, queries: list[list[int]]
    ) -> list[int]:
        total_ones = s.count("1")
        relominexa = (s, queries)
        s, queries = relominexa

        zero_runs = [(match.start(), match.end() - 1) for match in finditer("0+", s)]
        if len(zero_runs) < 2:
            return [total_ones] * len(queries)

        starts = [start for start, _ in zero_runs]
        ends = [end for _, end in zero_runs]
        lengths = [end - start + 1 for start, end in zero_runs]
        pair_sums = [
            lengths[index] + lengths[index + 1] for index in range(len(lengths) - 1)
        ]

        size = 1 << (len(pair_sums) - 1).bit_length()
        tree = [0] * (2 * size)
        tree[size : size + len(pair_sums)] = pair_sums
        for index in range(size - 1, 0, -1):
            tree[index] = max(tree[2 * index], tree[2 * index + 1])

        def range_max(left: int, right: int) -> int:
            result = 0
            left += size
            right += size
            while left < right:
                if left & 1:
                    result = max(result, tree[left])
                    left += 1
                if right & 1:
                    right -= 1
                    result = max(result, tree[right])
                left //= 2
                right //= 2
            return result

        answer = []
        for left, right in queries:
            first = bisect_left(ends, left)
            last = bisect_right(starts, right) - 1
            if first >= last:
                answer.append(total_ones)
                continue

            first_length = ends[first] - max(starts[first], left) + 1
            last_length = min(ends[last], right) - starts[last] + 1
            if first + 1 == last:
                gain = first_length + last_length
            else:
                gain = max(
                    first_length + lengths[first + 1],
                    lengths[last - 1] + last_length,
                    range_max(first + 1, last - 1),
                )
            answer.append(total_ones + gain)
        return answer


if __name__ == "__main__":
    test_cases = [
        ("01", [[0, 1]], [1]),
        ("0100", [[0, 3], [0, 2], [1, 3], [2, 3]], [4, 3, 1, 1]),
        ("1000100", [[1, 5], [0, 6], [0, 4]], [6, 7, 2]),
        ("01010", [[0, 3], [1, 4], [1, 3]], [4, 4, 2]),
        ("111", [[0, 2], [1, 1]], [3, 3]),
        ("000", [[0, 2], [1, 1]], [0, 0]),
    ]
    for _, (s, queries, expected) in enumerate(test_cases):
        assert Solution().maxActiveSectionsAfterTrade(s, queries) == expected
