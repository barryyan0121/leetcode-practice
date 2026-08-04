"""3542. 将所有元素变为 0 的最少操作次数"""


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        stack = []
        operations = 0
        for value in nums:
            if value == 0:
                stack.clear()
                continue
            while stack and stack[-1] > value:
                stack.pop()
            if not stack or stack[-1] < value:
                stack.append(value)
                operations += 1
        return operations


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 1],), 2),
        (([2, 1, 2],), 3),
        (([0, 2, 0, 2],), 2),
        (([0, 0],), 0),
    ]
    for _, ((nums,), expected) in enumerate(test_cases):
        assert Solution().minOperations(nums) == expected
