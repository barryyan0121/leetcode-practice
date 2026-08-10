"""2183. 统计可以被 K 整除的下标对数目"""

from collections import Counter
from math import gcd


class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        factors = Counter()
        answer = 0
        for value in nums:
            divisor = gcd(value, k)
            for previous, count in factors.items():
                if divisor * previous % k == 0:
                    answer += count
            factors[divisor] += 1
        return answer


if __name__ == "__main__":
    assert Solution().countPairs([1, 2, 3, 4, 5], 2) == 7
