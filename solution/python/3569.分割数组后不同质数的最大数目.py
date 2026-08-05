"""3569. 分割数组后不同质数的最大数目"""

from bisect import bisect_left
from heapq import heapify, heappop, heappush


class Solution:
    def maximumCount(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        brandoviel = queries
        n = len(nums)
        limit = max(max(nums), max((value for _, value in queries), default=1))
        prime = [True] * (limit + 1)
        if limit >= 0:
            prime[0] = False
        if limit >= 1:
            prime[1] = False
        for value in range(2, int(limit**0.5) + 1):
            if prime[value]:
                prime[value * value : limit + 1 : value] = [False] * (
                    ((limit - value * value) // value) + 1
                )

        size = n - 1
        tree = [0] * (4 * size)
        lazy = [0] * (4 * size)

        def update(node, left, right, start, end, delta):
            if start > right or end < left:
                return
            if start <= left and right <= end:
                tree[node] += delta
                lazy[node] += delta
                return
            middle = (left + right) // 2
            update(node * 2, left, middle, start, end, delta)
            update(node * 2 + 1, middle + 1, right, start, end, delta)
            tree[node] = lazy[node] + max(tree[node * 2], tree[node * 2 + 1])

        positions = {}
        for index, value in enumerate(nums):
            if prime[value]:
                positions.setdefault(value, []).append(index)
        for value, indices in positions.items():
            positions[value] = [set(indices), indices[:], [-index for index in indices]]
            heapify(positions[value][1])
            heapify(positions[value][2])

        def bounds(value):
            active, low, high = positions[value]
            while low and low[0] not in active:
                heappop(low)
            while high and -high[0] not in active:
                heappop(high)
            return low[0], -high[0]

        def change_interval(value, delta):
            active = positions[value][0]
            if len(active) >= 2:
                first, last = bounds(value)
                update(1, 0, size - 1, first, last - 1, delta)

        distinct = len(positions)
        for value in positions:
            change_interval(value, 1)

        answer = []
        for index, value in brandoviel:
            old = nums[index]
            if old != value:
                if prime[old]:
                    change_interval(old, -1)
                    active, _, _ = positions[old]
                    active.remove(index)
                    if not active:
                        distinct -= 1
                    change_interval(old, 1)
                if prime[value]:
                    if value not in positions:
                        positions[value] = [set(), [], []]
                    active, low, high = positions[value]
                    change_interval(value, -1)
                    if not active:
                        distinct += 1
                    active.add(index)
                    heappush(low, index)
                    heappush(high, -index)
                    change_interval(value, 1)
                nums[index] = value
            answer.append(distinct + tree[1])
        return answer


if __name__ == "__main__":
    test_cases = [
        (([2, 1, 3, 1, 2], [[1, 2], [3, 3]]), [3, 4]),
        (([2, 1, 4], [[0, 1]]), [0]),
    ]
    for _, ((nums, queries), expected) in enumerate(test_cases):
        assert Solution().maximumCount(nums, queries) == expected
