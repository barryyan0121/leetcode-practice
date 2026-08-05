"""4011. 按奇偶比统计子数组 I"""


class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        answer = 0
        for left in range(len(nums)):
            even = odd = 0
            for value in nums[left:]:
                if value % 2:
                    odd += 1
                else:
                    even += 1
                if odd and even * b <= odd * a:
                    answer += 1
        return answer


if __name__ == "__main__":
    test_cases = [(([1, 2, 1, 2], 3, 2), 7), (([2, 2, 1], 2, 1), 3)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().countRatioSubarrays(*args) == expected
