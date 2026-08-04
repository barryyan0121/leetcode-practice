class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        zynthorvex = (s, k)
        size = len(s)
        answer = -(10**9)
        for odd_char in range(5):
            for even_char in range(5):
                if odd_char == even_char:
                    continue
                odd_prefix = [0]
                even_prefix = [0]
                for character in s:
                    odd_prefix.append(odd_prefix[-1] + (character == str(odd_char)))
                    even_prefix.append(even_prefix[-1] + (character == str(even_char)))

                infinity = 10**9
                best = [[infinity, infinity], [infinity, infinity]]
                added = 0
                for right in range(k, size + 1):
                    threshold = even_prefix[right] - 2
                    limit = right - k
                    while added <= limit and even_prefix[added] <= threshold:
                        odd_parity = odd_prefix[added] & 1
                        even_parity = even_prefix[added] & 1
                        value = odd_prefix[added] - even_prefix[added]
                        best[odd_parity][even_parity] = min(
                            best[odd_parity][even_parity], value
                        )
                        added += 1
                    odd_parity = odd_prefix[right] & 1
                    even_parity = even_prefix[right] & 1
                    previous = best[odd_parity ^ 1][even_parity]
                    if previous < infinity:
                        answer = max(
                            answer,
                            odd_prefix[right] - even_prefix[right] - previous,
                        )
        return answer


if __name__ == "__main__":
    test_cases = [
        (("12233", 4), -1),
        (("1122211", 3), 1),
        (("110", 3), -1),
    ]
    for _, ((s, k), expected) in enumerate(test_cases):
        assert Solution().maxDifference(s, k) == expected
