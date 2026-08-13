"""3229. 使数组等于目标数组的最少操作次数"""


class Solution:
    def minimumOperations(self, nums: list[int], target: list[int]) -> int:
        answer = abs(target[0] - nums[0])
        for index in range(1, len(nums)):
            current = target[index] - nums[index]
            previous = target[index - 1] - nums[index - 1]
            if current >= 0 and previous >= 0:
                answer += max(0, current - previous)
            elif current <= 0 and previous <= 0:
                answer += max(0, abs(current) - abs(previous))
            else:
                answer += abs(current)
        return answer


if __name__ == "__main__":
    test_cases = [
        (([3, 5, 1, 2], [4, 6, 2, 4]), 2),
        (([1, 3, 2], [2, 1, 4]), 5),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minimumOperations(*args) == expected
