"""2376. 统计特殊整数"""


class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        digits = list(map(int, str(n)))
        memo = {}

        def dfs(pos: int, mask: int, limited: bool, started: bool) -> int:
            if pos == len(digits):
                return int(started)
            key = (pos, mask, limited, started)
            if key in memo:
                return memo[key]
            answer = 0
            upper = digits[pos] if limited else 9
            for value in range(upper + 1):
                if not started and value == 0:
                    answer += dfs(
                        pos + 1, mask, limited and value == digits[pos], False
                    )
                elif not mask >> value & 1:
                    answer += dfs(
                        pos + 1,
                        mask | 1 << value,
                        limited and value == digits[pos],
                        True,
                    )
            memo[key] = answer
            return answer

        return dfs(0, 0, True, False)

if __name__ == "__main__":
    assert Solution().countSpecialNumbers(20) == 19
