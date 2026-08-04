import heapq


class Solution:
    def maxRemoval(self, nums: list[int], queries: list[list[int]]) -> int:
        queries.sort()
        available = []
        selected_ending = [0] * (len(nums) + 1)
        active = 0
        used = 0
        query_index = 0

        for index, required in enumerate(nums):
            active += selected_ending[index]
            while query_index < len(queries) and queries[query_index][0] <= index:
                heapq.heappush(available, -queries[query_index][1])
                query_index += 1
            while active < required:
                while available and -available[0] < index:
                    heapq.heappop(available)
                if not available:
                    return -1
                end = -heapq.heappop(available)
                active += 1
                selected_ending[end + 1] -= 1
                used += 1
        return len(queries) - used


if __name__ == "__main__":
    test_cases = [
        (([2, 0, 2], [[0, 2], [0, 2], [1, 1]]), 1),
        (([1, 1, 1, 1], [[1, 3], [0, 2], [1, 3], [1, 2]]), 2),
        (([1, 2], [[0, 0]]), -1),
    ]
    for _, ((nums, queries), expected) in enumerate(test_cases):
        assert Solution().maxRemoval(nums, queries) == expected
