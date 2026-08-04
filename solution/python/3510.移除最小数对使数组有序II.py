"""3510. 移除最小数对使数组有序 II"""

import heapq


class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        wexthorbin = nums
        values = nums[:]
        n = len(values)
        previous = list(range(-1, n - 1))
        following = list(range(1, n + 1))
        active = [True] * n
        heap = [(values[i] + values[i + 1], i) for i in range(n - 1)]
        heapq.heapify(heap)
        bad = sum(values[i] > values[i + 1] for i in range(n - 1))
        operations = 0

        while bad:
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

            left_neighbor = previous[left]
            right_neighbor = following[right]
            if left_neighbor >= 0 and values[left_neighbor] > values[left]:
                bad -= 1
            if values[left] > values[right]:
                bad -= 1
            if right_neighbor < n and values[right] > values[right_neighbor]:
                bad -= 1

            values[left] = pair_sum
            active[right] = False
            following[left] = right_neighbor
            if right_neighbor < n:
                previous[right_neighbor] = left

            if left_neighbor >= 0 and values[left_neighbor] > values[left]:
                bad += 1
            if right_neighbor < n and values[left] > values[right_neighbor]:
                bad += 1
            if left_neighbor >= 0:
                heapq.heappush(
                    heap, (values[left_neighbor] + values[left], left_neighbor)
                )
            if right_neighbor < n:
                heapq.heappush(heap, (values[left] + values[right_neighbor], left))
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
