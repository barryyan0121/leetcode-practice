from bisect import bisect_left
from typing import List


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        answer = 0
        for bit in range(31):
            tails = []
            for value in nums:
                if value >> bit & 1:
                    i = bisect_left(tails, value)
                    if i == len(tails):
                        tails.append(value)
                    else:
                        tails[i] = value
            answer = max(answer, len(tails))
        return answer


if __name__ == "__main__":
    assert Solution().longestSubsequence([3, 1, 2, 4]) == 1
