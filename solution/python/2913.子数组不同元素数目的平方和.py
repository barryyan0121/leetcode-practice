"""2913. 子数组不同元素数目的平方和"""


class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        answer = 0
        for left in range(len(nums)):
            seen = set()
            for right in range(left, len(nums)):
                seen.add(nums[right])
                answer += len(seen) ** 2
        return answer


if __name__ == "__main__":
    assert Solution().sumCounts([1, 2, 1]) == 15
