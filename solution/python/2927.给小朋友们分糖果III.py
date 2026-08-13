class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def combinations(total: int) -> int:
            return (total + 2) * (total + 1) // 2 if total >= 0 else 0

        answer = combinations(n)
        answer -= 3 * combinations(n - limit - 1)
        answer += 3 * combinations(n - 2 * (limit + 1))
        answer -= combinations(n - 3 * (limit + 1))
        return answer


assert Solution().distributeCandies(5, 2) == 3
