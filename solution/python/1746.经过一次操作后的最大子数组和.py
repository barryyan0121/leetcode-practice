from typing import List


class Solution:
    def maxSumAfterOperation(self, nums: List[int], x: int) -> int:
        no_operation = nums[0]
        operation = nums[0] * x
        answer = operation
        for value in nums[1:]:
            operation = max(operation + value, no_operation + value * x, value * x)
            no_operation = max(no_operation + value, value)
            answer = max(answer, operation)
        return answer


if __name__ == "__main__":
    solution = Solution()
    assert solution.maxSumAfterOperation([2, -3, -1, -4, -2], -3) == 12
    print("1746 passed")
