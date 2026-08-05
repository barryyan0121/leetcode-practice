"""2562. 找出数组的串联值"""


class Solution:
    def findTheArrayConcVal(self, nums: list[int]) -> int:
        answer = 0
        left, right = 0, len(nums) - 1
        while left <= right:
            answer += int(str(nums[left]) + (str(nums[right]) if left != right else ""))
            left += 1
            right -= 1
        return answer


if __name__ == "__main__":
    test_cases = [(([7, 52, 2, 4],), 596)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().findTheArrayConcVal(*args) == expected
