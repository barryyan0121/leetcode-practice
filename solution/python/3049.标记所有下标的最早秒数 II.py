import heapq


class Solution:
    def earliestSecondToMarkIndices(
        self, nums: list[int], change_indices: list[int]
    ) -> int:
        length = len(nums)
        seconds = len(change_indices)
        last = [-1] * length
        for time in range(seconds - 1, -1, -1):
            last[change_indices[time] - 1] = time
        required = sum(nums) + length

        def feasible(end: int) -> bool:
            if any(position < 0 or position > end for position in last):
                return False
            remaining = required
            free = 0
            selected = []
            for time in range(end, -1, -1):
                index = change_indices[time] - 1
                if nums[index] <= 1:
                    free += 1
                    continue
                if time != last[index]:
                    free += 1
                    continue
                if free == 0:
                    if not selected or selected[0] >= nums[index]:
                        free += 1
                        continue
                    free += 2
                    remaining += selected[0] - 1
                    heapq.heappop(selected)
                free -= 1
                remaining -= nums[index] - 1
                heapq.heappush(selected, nums[index])
            return remaining <= end + 1

        left, right = 0, seconds - 1
        answer = -1
        while left <= right:
            middle = (left + right) // 2
            if feasible(middle):
                answer = middle + 1
                right = middle - 1
            else:
                left = middle + 1
        return answer


if __name__ == "__main__":
    test_cases = [
        (([3, 2, 3], [1, 3, 2, 2, 2, 2, 3]), 6),
        (([1, 2, 3], [1, 2, 3]), -1),
    ]
    for _, ((nums, change_indices), expected) in enumerate(test_cases):
        assert Solution().earliestSecondToMarkIndices(nums, change_indices) == expected
