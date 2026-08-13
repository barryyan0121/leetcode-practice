class Solution:
    def numberOfWays(
        self, n: int, m: int, k: int, source: list[int], dest: list[int]
    ) -> int:
        mod = 10**9 + 7

        def counts(length: int, start: int, target: int) -> list[int]:
            current = [0] * length
            current[start - 1] = 1
            result = [int(start == target)]
            for _ in range(k):
                total = sum(current) % mod
                current = [(total - value) % mod for value in current]
                result.append(current[target - 1])
            return result

        vertical = counts(n, source[0], dest[0])
        horizontal = counts(m, source[1], dest[1])
        combinations = [1]
        for i in range(k):
            combinations.append(
                combinations[-1] * (k - i) * pow(i + 1, mod - 2, mod) % mod
            )
        return (
            sum(combinations[i] * vertical[i] * horizontal[k - i] for i in range(k + 1))
            % mod
        )


assert Solution().numberOfWays(3, 2, 2, [1, 1], [2, 2]) == 2
