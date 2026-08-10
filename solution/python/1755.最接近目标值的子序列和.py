from bisect import bisect_left
from typing import List


class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        mid = len(nums) // 2

        def sums(values: List[int]) -> List[int]:
            result = [0]
            for value in values:
                result += [current + value for current in result]
            return result

        left = sums(nums[:mid])
        right = sorted(sums(nums[mid:]))
        answer = abs(goal)
        for value in left:
            index = bisect_left(right, goal - value)
            for candidate in right[max(0, index - 1) : index + 1]:
                answer = min(answer, abs(value + candidate - goal))
        return answer


if __name__ == "__main__":
    solution = Solution()
    assert solution.minAbsDifference([5, -7, 3, 5], 6) == 0
    assert solution.minAbsDifference([7, -9, 15, -2], -5) == 1
    print("1755 passed")
