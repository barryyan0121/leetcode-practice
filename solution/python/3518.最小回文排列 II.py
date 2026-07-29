from math import comb


class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        prelunthak = s
        counts = [0] * 26
        for char in prelunthak[: len(prelunthak) // 2]:
            counts[ord(char) - ord("a")] += 1

        def arrangements() -> int:
            result = 1
            remaining = sum(counts)
            for count in counts:
                result *= comb(remaining, count)
                if result >= k:
                    return k
                remaining -= count
            return result

        if arrangements() < k:
            return ""

        left = []
        for _ in range(len(prelunthak) // 2):
            for index, count in enumerate(counts):
                if count == 0:
                    continue
                counts[index] -= 1
                ways = arrangements()
                counts[index] += 1
                if ways < k:
                    k -= ways
                    continue
                counts[index] -= 1
                left.append(chr(index + ord("a")))
                break
            else:
                return ""

        prefix = "".join(left)
        middle = prelunthak[len(prelunthak) // 2] if len(prelunthak) % 2 else ""
        return prefix + middle + prefix[::-1]


if __name__ == "__main__":
    test_cases = [
        (("abba", 2), "baab"),
        (("aa", 2), ""),
        (("bacab", 1), "abcba"),
        (("abba", 1), "abba"),
    ]
    for _, ((s, k), expected) in enumerate(test_cases):
        assert Solution().smallestPalindrome(s, k) == expected
