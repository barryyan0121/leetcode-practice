from math import gcd


class Solution:
    def maxGcdSum(self, nums: list[int], k: int) -> int:
        prefix = [0]
        for value in nums:
            prefix.append(prefix[-1] + value)
        groups = []
        answer = 0
        for right, value in enumerate(nums):
            next_groups = [(value, right, right)]
            for current_gcd, left, end in groups:
                new_gcd = gcd(current_gcd, value)
                if next_groups[-1][0] == new_gcd:
                    next_groups[-1] = (new_gcd, left, end)
                else:
                    next_groups.append((new_gcd, left, end))
            groups = next_groups
            latest_start = right - k + 1
            for current_gcd, left, _ in groups:
                if left <= latest_start:
                    answer = max(
                        answer, current_gcd * (prefix[right + 1] - prefix[left])
                    )
        return answer


if __name__ == "__main__":
    assert Solution().maxGcdSum([2, 1, 4, 4, 4, 2], 2) == 48
