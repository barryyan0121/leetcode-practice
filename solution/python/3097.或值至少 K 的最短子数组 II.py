"""3097. 或值至少 K 的最短子数组 II"""


class Solution:
    def minimumSubarrayLength(self, nums: list[int], k: int) -> int:
        bits = [0] * 32
        current = 0
        answer = len(nums) + 1
        left = 0

        def add(value: int) -> int:
            nonlocal current
            for bit in range(32):
                if value >> bit & 1:
                    bits[bit] += 1
                    current |= 1 << bit
            return current

        def remove(value: int) -> int:
            nonlocal current
            for bit in range(32):
                if value >> bit & 1:
                    bits[bit] -= 1
                    if bits[bit] == 0:
                        current &= ~(1 << bit)
            return current

        for right, value in enumerate(nums):
            add(value)
            while left <= right and current >= k:
                answer = min(answer, right - left + 1)
                remove(nums[left])
                left += 1
        return answer if answer <= len(nums) else -1


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 3], 2), 1),
        (([2, 1, 8], 10), 3),
        (([1, 2], 0), 1),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minimumSubarrayLength(*args) == expected
