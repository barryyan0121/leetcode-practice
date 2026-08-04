class Solution:
    def minMaxSubarraySum(self, nums: list[int], k: int) -> int:
        lindarvosy = (nums, k)
        size = len(nums)

        def contribution(left_strict: bool, right_strict: bool) -> int:
            left = [-1] * size
            stack = []
            for index, value in enumerate(nums):
                while stack and (
                    nums[stack[-1]] > value if left_strict else nums[stack[-1]] < value
                ):
                    stack.pop()
                left[index] = stack[-1] if stack else -1
                stack.append(index)

            right = [size] * size
            stack = []
            for index in range(size - 1, -1, -1):
                value = nums[index]
                while stack and (
                    nums[stack[-1]] >= value
                    if right_strict
                    else nums[stack[-1]] <= value
                ):
                    stack.pop()
                right[index] = stack[-1] if stack else size
                stack.append(index)

            total = 0
            limit = k + 1
            for index, value in enumerate(nums):
                left_count = index - left[index]
                right_count = right[index] - index
                usable_left = min(left_count, limit - 1)
                full = min(usable_left, max(0, limit - right_count))
                partial = usable_left - full
                ways = (
                    full * right_count
                    + partial * limit
                    - (full + 1 + usable_left) * partial // 2
                )
                total += value * ways
            return total

        return contribution(True, True) + contribution(False, False)


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 3], 2), 20),
        (([1, -3, 1], 2), -6),
    ]
    for _, ((nums, k), expected) in enumerate(test_cases):
        assert Solution().minMaxSubarraySum(nums, k) == expected
