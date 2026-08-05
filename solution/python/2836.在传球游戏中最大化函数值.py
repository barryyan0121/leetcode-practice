class Solution:
    def getMaxFunctionValue(self, receiver: list[int], k: int) -> int:
        n = len(receiver)
        log = k.bit_length()
        nxt = [[0] * n for _ in range(log)]
        total = [[0] * n for _ in range(log)]
        for i, v in enumerate(receiver):
            nxt[0][i], total[0][i] = v, v
        for b in range(1, log):
            for i in range(n):
                mid = nxt[b - 1][i]
                nxt[b][i] = nxt[b - 1][mid]
                total[b][i] = total[b - 1][i] + total[b - 1][mid]
        ans = 0
        for start in range(n):
            cur = start
            score = start
            steps = k
            bit = 0
            while steps:
                if steps & 1:
                    score += total[bit][cur]
                    cur = nxt[bit][cur]
                steps >>= 1
                bit += 1
            ans = max(ans, score)
        return ans


if __name__ == "__main__":
    assert Solution().getMaxFunctionValue([2, 0, 1], 4) == 6
