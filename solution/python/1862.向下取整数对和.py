from typing import List


class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        maximum = max(nums)
        frequency = [0] * (maximum + 1)
        for value in nums:
            frequency[value] += 1
        prefix = [0] * (maximum + 1)
        for value in range(1, maximum + 1):
            prefix[value] = prefix[value - 1] + frequency[value]
        answer = 0
        for divisor in range(1, maximum + 1):
            if frequency[divisor] == 0:
                continue
            multiple = divisor
            quotient = 1
            while multiple <= maximum:
                answer += (
                    frequency[divisor]
                    * quotient
                    * (
                        prefix[min(multiple + divisor - 1, maximum)]
                        - prefix[multiple - 1]
                    )
                )
                multiple += divisor
                quotient += 1
        return answer % mod

if __name__ == "__main__":
    assert Solution().sumOfFlooredPairs([2, 5, 9]) == 10
