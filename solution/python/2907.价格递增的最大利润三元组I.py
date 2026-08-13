class Solution:
    def maxProfit(self, prices: list[int], profits: list[int]) -> int:
        n = len(prices)
        answer = -1
        for middle in range(1, n - 1):
            left = max(
                (profits[i] for i in range(middle) if prices[i] < prices[middle]),
                default=-1,
            )
            right = max(
                (
                    profits[i]
                    for i in range(middle + 1, n)
                    if prices[i] > prices[middle]
                ),
                default=-1,
            )
            if left >= 0 and right >= 0:
                answer = max(answer, left + profits[middle] + right)
        return answer


assert Solution().maxProfit([10, 2, 3, 4], [100, 2, 7, 10]) == 19
