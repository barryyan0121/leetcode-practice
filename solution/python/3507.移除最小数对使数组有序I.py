"""3507. 移除最小数对使数组有序 I"""

import heapq


class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        values = nums[:]
        n = len(values)
        previous = list(range(-1, n - 1))
        following = list(range(1, n + 1))
        active = [True] * n
        heap = [(values[i] + values[i + 1], i) for i in range(n - 1)]
        heapq.heapify(heap)

        def is_sorted() -> bool:
            i = 0
            while following[i] < n:
                if values[i] > values[following[i]]:
                    return False
                i = following[i]
            return True

        operations = 0
        while not is_sorted():
            pair_sum, left = heapq.heappop(heap)
            right = following[left]
            while (
                not active[left]
                or right == n
                or not active[right]
                or values[left] + values[right] != pair_sum
            ):
                pair_sum, left = heapq.heappop(heap)
                right = following[left]
            values[left] = pair_sum
            active[right] = False
            following[left] = following[right]
            if following[right] < n:
                previous[following[right]] = left
            left_neighbor = previous[left]
            if left_neighbor >= 0:
                heapq.heappush(
                    heap, (values[left_neighbor] + values[left], left_neighbor)
                )
            if following[left] < n:
                heapq.heappush(heap, (values[left] + values[following[left]], left))
            operations += 1
        return operations


if __name__ == "__main__":
    test_cases = [
        (([5, 2, 3, 1]), 2),
        (([1, 2, 3]), 0),
        (([2, 1, 1, 3]), 1),
    ]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().minimumPairRemoval(nums) == expected
