"""2488. 统计中位数为 K 的子数组"""


class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        pivot = nums.index(k)
        counts = {0: 1}
        balance = 0
        for index in range(pivot - 1, -1, -1):
            balance += 1 if nums[index] > k else -1
            counts[balance] = counts.get(balance, 0) + 1
        answer = 0
        balance = 0
        for index in range(pivot, len(nums)):
            if index > pivot:
                balance += 1 if nums[index] > k else -1
            answer += counts.get(-balance, 0) + counts.get(1 - balance, 0)
        return answer

if __name__ == "__main__":
    assert Solution().countSubarrays([3,2,1,4,5], 4) == 3
