"""3480. 删除一个冲突对后最大子数组数目"""


class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: list[list[int]]) -> int:
        thornibrax = (n, conflictingPairs)
        by_left = [[] for _ in range(n + 1)]
        for pair_id, (first, second) in enumerate(conflictingPairs):
            left, right = sorted((first, second))
            by_left[left].append((right, pair_id))

        gains = [0] * len(conflictingPairs)
        answer = 0
        smallest = None
        second_smallest = None
        for left in range(n, 0, -1):
            for right, pair_id in by_left[left]:
                candidate = (right, pair_id)
                if smallest is None or candidate < smallest:
                    second_smallest = smallest
                    smallest = candidate
                elif second_smallest is None or candidate < second_smallest:
                    second_smallest = candidate
            if smallest is None:
                answer += n - left + 1
            else:
                answer += smallest[0] - left
                replacement = (
                    second_smallest[0] if second_smallest is not None else n + 1
                )
                gains[smallest[1]] += replacement - smallest[0]
        return answer + max(gains)


if __name__ == "__main__":
    test_cases = [
        ((4, [[2, 3], [1, 4]]), 9),
        ((5, [[1, 2], [2, 5], [3, 5]]), 12),
    ]
    for _, ((n, conflicting_pairs), expected) in enumerate(test_cases):
        assert Solution().maxSubarrays(n, conflicting_pairs) == expected
