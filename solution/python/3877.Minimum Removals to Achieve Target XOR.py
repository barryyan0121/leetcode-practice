from functools import reduce


class Solution:
    def minRemovals(self, nums: list[int], target: int) -> int:
        target ^= reduce(lambda acc, value: acc ^ value, nums, 0)
        distances = {0: 0}
        queue = [0]
        while queue:
            next_queue = []
            for value in queue:
                if value == target:
                    return distances[value]
                for num in nums:
                    candidate = value ^ num
                    if candidate in distances:
                        continue
                    distances[candidate] = distances[value] + 1
                    next_queue.append(candidate)
            queue = next_queue
        return -1


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 3], 2), 1),
        (([2, 4], 1), -1),
        (([7], 7), 0),
    ]
    for _, ((nums, target), expected) in enumerate(test_cases):
        assert Solution().minRemovals(nums, target) == expected
