"""3589. 计数质数间隔平衡子数组"""

from collections import deque


class Solution:
    def primeSubarray(self, nums: list[int], k: int) -> int:
        zelmoricad = nums
        limit = max(nums)
        prime = [True] * (limit + 1)
        if limit >= 0:
            prime[0] = False
        if limit >= 1:
            prime[1] = False
        for value in range(2, int(limit**0.5) + 1):
            if prime[value]:
                prime[value * value : limit + 1 : value] = [False] * (
                    ((limit - value * value) // value) + 1
                )
        positions = [i for i, value in enumerate(nums) if prime[value]]
        count = len(positions)
        if count < 2:
            return 0
        values = [nums[i] for i in positions]
        first_choices = [
            positions[i] - (positions[i - 1] if i else -1) for i in range(count)
        ]
        prefix = [0]
        for choices in first_choices:
            prefix.append(prefix[-1] + choices)
        last_choices = [
            (positions[i + 1] if i + 1 < count else len(nums)) - positions[i]
            for i in range(count)
        ]
        minimum, maximum = deque(), deque()
        left = 0
        answer = 0
        for right, value in enumerate(values):
            while minimum and values[minimum[-1]] >= value:
                minimum.pop()
            while maximum and values[maximum[-1]] <= value:
                maximum.pop()
            minimum.append(right)
            maximum.append(right)
            while values[maximum[0]] - values[minimum[0]] > k:
                if minimum[0] == left:
                    minimum.popleft()
                if maximum[0] == left:
                    maximum.popleft()
                left += 1
            if right > left:
                answer += (prefix[right] - prefix[left]) * last_choices[right]
        return answer


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 3], 1), 2),
        (([2, 3, 5, 7], 3), 4),
    ]
    for _, ((nums, k), expected) in enumerate(test_cases):
        assert Solution().primeSubarray(nums, k) == expected
