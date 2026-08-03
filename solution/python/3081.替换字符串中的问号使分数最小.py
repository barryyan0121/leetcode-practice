import heapq


class Solution:
    def minimizeStringValue(self, s: str) -> str:
        counts = [0] * 26
        for character in s:
            if character != "?":
                counts[ord(character) - ord("a")] += 1
        heap = [(count, chr(ord("a") + index)) for index, count in enumerate(counts)]
        heapq.heapify(heap)
        replacements = []
        for character in s:
            if character != "?":
                continue
            count, replacement = heapq.heappop(heap)
            replacements.append(replacement)
            heapq.heappush(heap, (count + 1, replacement))
        replacements.sort()
        iterator = iter(replacements)
        return "".join(
            next(iterator) if character == "?" else character for character in s
        )


if __name__ == "__main__":
    test_cases = [("???", "abc"), ("a?a?", "abac")]
    for _, (s, expected) in enumerate(test_cases):
        assert Solution().minimizeStringValue(s) == expected
