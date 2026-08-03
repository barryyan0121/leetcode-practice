import heapq


class Solution:
    def clearStars(self, s: str) -> str:
        heap = []
        removed = [False] * len(s)
        for index, character in enumerate(s):
            if character == "*":
                removed[index] = True
                _, _, remove_index = heapq.heappop(heap)
                removed[remove_index] = True
            else:
                heapq.heappush(heap, (character, -index, index))
        return "".join(
            character for index, character in enumerate(s) if not removed[index]
        )


if __name__ == "__main__":
    test_cases = [("aaba*", "aab"), ("abc*d*", "b")]
    for _, (s, expected) in enumerate(test_cases):
        assert Solution().clearStars(s) == expected
