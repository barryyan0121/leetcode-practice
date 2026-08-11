class Solution:
    def beautifulSplits(self, nums: list[int]) -> int:
        n = len(nums)
        z = [0] * n
        left = right = 0
        for i in range(1, n):
            if i <= right:
                z[i] = min(right - i + 1, z[i - left])
            while i + z[i] < n and nums[z[i]] == nums[i + z[i]]:
                z[i] += 1
            if i + z[i] - 1 > right:
                left, right = i, i + z[i] - 1

        answer = 0
        for gap in range(1, n):
            common = 0
            for first in range(n - gap - 1, -1, -1):
                second = first + gap
                common = common + 1 if nums[first] == nums[second] else 0
                if (
                    second < n
                    and first > 0
                    and ((first <= gap and z[first] >= first) or (second + gap <= n and common >= gap))
                ):
                    answer += 1
        return answer


if __name__ == "__main__":
    test_cases = [(([1, 1, 2, 1],), 2), (([1, 2, 3, 4],), 0)]
    for _, ((nums,), expected) in enumerate(test_cases):
        assert Solution().beautifulSplits(nums) == expected
