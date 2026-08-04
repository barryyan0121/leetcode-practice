class Solution:
    def countWinningSequences(self, s: str) -> int:
        mod = 10**9 + 7
        creatures = "FWE"
        beats = {("F", "E"), ("W", "F"), ("E", "W")}
        offset = len(s)
        previous = [[0] * 4 for _ in range(2 * offset + 1)]
        previous[offset][3] = 1
        for alice in s:
            current = [[0] * 4 for _ in range(2 * offset + 1)]
            for score, counts in enumerate(previous):
                for last, count in enumerate(counts):
                    if count == 0:
                        continue
                    for move_index, bob in enumerate(creatures):
                        if move_index == last:
                            continue
                        change = (
                            0 if bob == alice else (1 if (bob, alice) in beats else -1)
                        )
                        current[score + change][move_index] = (
                            current[score + change][move_index] + count
                        ) % mod
            previous = current
        return sum(sum(counts[:3]) for counts in previous[offset + 1 :]) % mod


if __name__ == "__main__":
    test_cases = [
        (("FFF",), 3),
        (("FWEFW",), 18),
    ]
    for _, ((s,), expected) in enumerate(test_cases):
        assert Solution().countWinningSequences(s) == expected
