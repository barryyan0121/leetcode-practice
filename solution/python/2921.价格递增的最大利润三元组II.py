class Solution:
    def maxProfit(self, prices: list[int], profits: list[int]) -> int:
        n = len(prices)
        left = [-1] * n
        candidates = []
        for i in range(n):
            while candidates and prices[candidates[-1]] >= prices[i]:
                candidates.pop()
            if candidates:
                left[i] = max(profits[j] for j in candidates)
            candidates.append(i)
        right = [-1] * n
        candidates = []
        for i in range(n - 1, -1, -1):
            while candidates and prices[candidates[-1]] <= prices[i]:
                candidates.pop()
            if candidates:
                right[i] = max(profits[j] for j in candidates)
            candidates.append(i)
        return max(
            (
                left[i] + profits[i] + right[i]
                for i in range(n)
                if left[i] >= 0 and right[i] >= 0
            ),
            default=-1,
        )


assert Solution().maxProfit([10, 2, 3, 4], [100, 2, 7, 10]) == 19
