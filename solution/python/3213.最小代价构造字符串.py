class Solution:
    def minimumCost(self, target: str, words: list[str], costs: list[int]) -> int:
        if len(set(target)) == 1:
            same_costs = {}
            character = target[0]
            for word, cost in zip(words, costs):
                if all(item == character for item in word):
                    length = len(word)
                    same_costs[length] = min(same_costs.get(length, cost), cost)
            infinity = 10**18
            dp = [0] + [infinity] * len(target)
            same_length_data = sorted(same_costs.items())
            for end in range(1, len(target) + 1):
                for length, cost in same_length_data:
                    if length > end:
                        break
                    dp[end] = min(dp[end], dp[end - length] + cost)
            return -1 if dp[-1] == infinity else dp[-1]

        mask, base = (1 << 64) - 1, 911_382_323
        lengths = {}
        for word, cost in zip(words, costs):
            word_hash = 0
            for character in word:
                word_hash = (word_hash * base + ord(character) - 96) & mask
            length = len(word)
            costs_by_hash = lengths.setdefault(length, {})
            costs_by_hash[word_hash] = min(costs_by_hash.get(word_hash, cost), cost)

        maximum = len(target)
        powers = [1] * (maximum + 1)
        for index in range(maximum):
            powers[index + 1] = powers[index] * base & mask

        prefix = [0] * (maximum + 1)
        for index, character in enumerate(target):
            prefix[index + 1] = (prefix[index] * base + ord(character) - 96) & mask

        infinity = 10**18
        dp = [infinity] * (maximum + 1)
        dp[0] = 0
        length_data = sorted(lengths.items())
        for end in range(1, maximum + 1):
            best = infinity
            for length, costs_by_hash in length_data:
                start = end - length
                if start < 0:
                    break
                if start < 0 or dp[start] == infinity:
                    continue
                key = (prefix[end] - prefix[start] * powers[length]) & mask
                cost = costs_by_hash.get(key)
                if cost is not None:
                    best = min(best, dp[start] + cost)
            dp[end] = best
        return -1 if dp[-1] == infinity else dp[-1]


if __name__ == "__main__":
    test_cases = [
        (("abcdef", ["abdef", "abc", "d", "def", "ef"], [100, 1, 1, 10, 5]), 7),
        (("aaaa", ["z", "zz", "zzz"], [1, 10, 100]), -1),
    ]
    for _, ((target, words, costs), expected) in enumerate(test_cases):
        assert Solution().minimumCost(target, words, costs) == expected
