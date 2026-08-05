import heapq


class Solution:
    def earliestSecondToMarkIndices(
        self, nums: list[int], change_indices: list[int]
    ) -> int:
        first_zero_second = {}
        seen = set()
        for second, index in enumerate(change_indices):
            index -= 1
            if nums[index] > 0 and index not in seen:
                first_zero_second[second] = index
                seen.add(index)
        total = sum(nums)

        def can_mark(max_second: int) -> bool:
            zero_candidates = []
            available_marks = 0
            for second in range(max_second - 1, -1, -1):
                if second in first_zero_second:
                    index = first_zero_second[second]
                    heapq.heappush(zero_candidates, nums[index])
                    if available_marks == 0:
                        heapq.heappop(zero_candidates)
                        available_marks += 1
                    else:
                        available_marks -= 1
                else:
                    available_marks += 1
            decrement_and_mark = (
                total - sum(zero_candidates) + len(nums) - len(zero_candidates)
            )
            zero_and_mark = 2 * len(zero_candidates)
            return decrement_and_mark + zero_and_mark <= max_second

        left, right = 0, len(change_indices) + 1
        while left < right:
            middle = (left + right) // 2
            if can_mark(middle):
                right = middle
            else:
                left = middle + 1
        return left if left <= len(change_indices) else -1


if __name__ == "__main__":
    test_cases = [
        (([3, 2, 3], [1, 3, 2, 2, 2, 2, 3]), 6),
        (([1, 2, 3], [1, 2, 3]), -1),
    ]
    for _, ((nums, change_indices), expected) in enumerate(test_cases):
        assert Solution().earliestSecondToMarkIndices(nums, change_indices) == expected
