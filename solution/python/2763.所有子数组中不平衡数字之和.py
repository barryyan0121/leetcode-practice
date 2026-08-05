class Solution:
    def sumImbalanceNumbers(self, nums: list[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            seen = set()
            imbalance = -1
            for value in nums[i:]:
                if value not in seen:
                    imbalance += value - 1 not in seen and value + 1 not in seen
                    imbalance -= value - 1 in seen and value + 1 in seen
                    seen.add(value)
                ans += imbalance
        return ans


if __name__ == "__main__":
    assert Solution().sumImbalanceNumbers([2, 3, 1, 4]) == 3
