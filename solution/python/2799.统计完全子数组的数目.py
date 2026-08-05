class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:
        total = len(set(nums))
        count = {}
        left = ans = 0
        for right, value in enumerate(nums):
            count[value] = count.get(value, 0) + 1
            while len(count) == total:
                ans += len(nums) - right
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1
        return ans


if __name__ == "__main__":
    assert Solution().countCompleteSubarrays([1, 3, 1, 2, 2]) == 4
