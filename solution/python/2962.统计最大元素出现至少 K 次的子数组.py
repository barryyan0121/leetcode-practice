"""2962. 统计最大元素出现至少 K 次的子数组"""


class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        maximum = max(nums)
        left = count = 0
        answer = 0
        for value in nums:
            count += value == maximum
            while count >= k:
                count -= nums[left] == maximum
                left += 1
            answer += left
        return answer


if __name__ == "__main__":
    assert Solution().countSubarrays([1, 3, 2, 3, 3], 2) == 6
