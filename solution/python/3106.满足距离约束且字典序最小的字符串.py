class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        result = list(s)
        for index, character in enumerate(result):
            distance = ord(character) - ord("a")
            to_a = min(distance, 26 - distance)
            if to_a <= k:
                result[index] = "a"
                k -= to_a
            else:
                result[index] = chr(ord(character) - k)
                break
        return "".join(result)


if __name__ == "__main__":
    test_cases = [("zbbz", 3, "aaaz"), ("xax", 2, "vax")]
    for _, (s, k, expected) in enumerate(test_cases):
        assert Solution().getSmallestString(s, k) == expected
