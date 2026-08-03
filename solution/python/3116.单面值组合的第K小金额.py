from math import gcd


class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        def count(amount: int) -> int:
            total = 0
            for mask in range(1, 1 << len(coins)):
                least_common_multiple = 1
                bits = 0
                for index, coin in enumerate(coins):
                    if mask >> index & 1:
                        bits += 1
                        least_common_multiple = (
                            least_common_multiple
                            // gcd(least_common_multiple, coin)
                            * coin
                        )
                        if least_common_multiple > amount:
                            break
                else:
                    contribution = amount // least_common_multiple
                    total += contribution if bits % 2 else -contribution
            return total

        left, right = 1, min(coins) * k
        while left < right:
            middle = (left + right) // 2
            if count(middle) >= k:
                right = middle
            else:
                left = middle + 1
        return left


if __name__ == "__main__":
    test_cases = [([3, 6, 9], 5, 15), ([5, 2], 7, 12)]
    for _, (coins, k, expected) in enumerate(test_cases):
        assert Solution().findKthSmallest(coins, k) == expected
