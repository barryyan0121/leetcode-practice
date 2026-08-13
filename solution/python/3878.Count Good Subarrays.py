class Solution:
    def countGoodSubarrays(self, nums: list[int]) -> int:
        def is_proper_subset(a: int, b: int) -> bool:
            return a != b and (a | b) == b

        def is_subset(a: int, b: int) -> bool:
            return (a | b) == b

        right = [len(nums)] * len(nums)
        stack: list[int] = []
        for i in range(len(nums) - 1, -1, -1):
            while stack and is_subset(nums[stack[-1]], nums[i]):
                stack.pop()
            right[i] = stack[-1] if stack else len(nums)
            stack.append(i)

        result = 0
        left = -1
        stack.clear()
        for i, num in enumerate(nums):
            while stack and is_proper_subset(nums[stack[-1]], num):
                stack.pop()
            left = stack[-1] if stack else -1
            stack.append(i)
            result += (i - left) * (right[i] - i)
        return result


if __name__ == "__main__":
    test_cases = [
        ([4, 2, 3], 4),
        ([1, 3, 1], 6),
    ]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().countGoodSubarrays(nums) == expected
