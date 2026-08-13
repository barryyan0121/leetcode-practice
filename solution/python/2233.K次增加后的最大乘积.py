"""2233. K 次增加后的最大乘积"""

import heapq


class Solution:
    def maximumProduct(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums)
        while k:
            value = heapq.heappop(nums)
            heapq.heappush(nums, value + 1)
            k -= 1
        answer = 1
        for value in nums:
            answer = answer * value % 1_000_000_007
        return answer


if __name__ == "__main__":
    assert Solution().maximumProduct([0, 4], 5) == 20
