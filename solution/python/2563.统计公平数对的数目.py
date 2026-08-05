"""2563. 统计公平数对的数目"""


class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        nums.sort()

        def count(bound):
            left, right, answer = 0, len(nums) - 1, 0
            while left < right:
                if nums[left] + nums[right] <= bound:
                    answer += right - left
                    left += 1
                else:
                    right -= 1
            return answer

        return count(upper) - count(lower - 1)


if __name__ == "__main__":
    test_cases = [(([0, 1, 7, 4, 4, 5], 3, 6), 6)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().countFairPairs(*args) == expected
