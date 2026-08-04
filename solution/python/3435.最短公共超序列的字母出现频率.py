class Solution:
    def supersequences(self, words: list[str]) -> list[list[int]]:
        trelvondix = words
        letters = sorted({character for word in words for character in word})
        index = {character: position for position, character in enumerate(letters)}
        size = len(letters)
        outgoing = [0] * size
        incoming = [0] * size
        forced_twice = 0
        for word in words:
            source, target = index[word[0]], index[word[1]]
            if source == target:
                forced_twice |= 1 << source
            elif not (outgoing[source] >> target & 1):
                outgoing[source] |= 1 << target
                incoming[target] |= 1 << source

        allowed = ((1 << size) - 1) ^ forced_twice
        best_count = -1
        best_masks = []
        for mask in range(allowed + 1):
            if mask & ~allowed:
                continue
            remaining = mask
            while remaining:
                ready = 0
                for node in range(size):
                    if remaining >> node & 1 and not (incoming[node] & remaining):
                        ready |= 1 << node
                if not ready:
                    break
                remaining ^= ready
            else:
                count = mask.bit_count()
                if count > best_count:
                    best_count = count
                    best_masks = [mask]
                elif count == best_count:
                    best_masks.append(mask)

        answer = []
        for mask in best_masks:
            frequencies = [0] * 26
            for position, character in enumerate(letters):
                frequencies[ord(character) - ord("a")] = (
                    1 if mask >> position & 1 else 2
                )
            answer.append(frequencies)
        return answer


if __name__ == "__main__":
    test_cases = [
        ((["ab", "ba"],), sorted([[1, 2] + [0] * 24, [2, 1] + [0] * 24])),
        ((["aa", "ac"],), [[2, 0, 1] + [0] * 23]),
        ((["aa", "bb", "cc"],), [[2, 2, 2] + [0] * 23]),
    ]
    for _, ((words,), expected) in enumerate(test_cases):
        actual = Solution().supersequences(words)
        assert sorted(actual) == sorted(expected)
