import heapq


class Solution:
    def minValidStrings(self, words: list[str], target: str) -> int:
        moduli = (1_000_000_007, 1_000_000_009)
        base = 911382323
        max_length = max(map(len, words + [target]))
        powers = [[1] * (max_length + 1) for _ in moduli]
        for index, modulus in enumerate(moduli):
            for length in range(max_length):
                powers[index][length + 1] = powers[index][length] * base % modulus

        prefixes = {}
        for word in words:
            hashes = [0, 0]
            for length, character in enumerate(word, 1):
                for index, modulus in enumerate(moduli):
                    hashes[index] = (hashes[index] * base + ord(character)) % modulus
                prefixes.setdefault(length, set()).add(tuple(hashes))

        target_hashes = [[0] * (len(target) + 1) for _ in moduli]
        for position, character in enumerate(target, 1):
            for index, modulus in enumerate(moduli):
                target_hashes[index][position] = (
                    target_hashes[index][position - 1] * base + ord(character)
                ) % modulus

        def substring_hash(start: int, end: int) -> tuple[int, int]:
            length = end - start
            return tuple(
                (
                    target_hashes[index][end]
                    - target_hashes[index][start] * powers[index][length]
                )
                % modulus
                for index, modulus in enumerate(moduli)
            )

        def longest_match(start: int) -> int:
            low, high = 0, len(target) - start
            while low < high:
                length = (low + high + 1) // 2
                if (
                    length in prefixes
                    and substring_hash(start, start + length) in prefixes[length]
                ):
                    low = length
                else:
                    high = length - 1
            return low

        infinity = len(target) + 1
        dp = [infinity] * (len(target) + 1)
        dp[0] = 0
        active = []
        for position in range(len(target)):
            while active and active[0][1] < position + 1:
                heapq.heappop(active)
            if dp[position] < infinity:
                reach = position + longest_match(position)
                if reach > position:
                    heapq.heappush(active, (dp[position] + 1, reach))
            if active:
                dp[position + 1] = active[0][0]
        return -1 if dp[-1] == infinity else dp[-1]


if __name__ == "__main__":
    test_cases = [
        ((["abc", "aaaaa", "bcdef"], "aabcdabc"), 3),
        ((["abababab", "ab"], "ababaababa"), 2),
        ((["abcdef"], "xyz"), -1),
    ]
    for _, ((words, target), expected) in enumerate(test_cases):
        assert Solution().minValidStrings(words, target) == expected
