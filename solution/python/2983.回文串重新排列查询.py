"""2983. 回文串重新排列查询"""


class Solution:
    def canMakePalindromeQueries(self, s: str, queries: list[list[int]]) -> list[bool]:
        n = len(s)
        mirrored_diffs = self._get_mirrored_diffs(s)
        counts = self._get_counts(s)
        answer = []

        def subtract(left: list[int], right: list[int]) -> list[int]:
            return [x - y for x, y in zip(left, right)]

        for a, b, c, d in queries:
            b += 1
            d += 1
            ra = n - a
            rb = n - b
            rc = n - c
            rd = n - d

            if (
                (min(a, rd) > 0 and mirrored_diffs[min(a, rd)] > 0)
                or (
                    n // 2 > max(b, rc)
                    and mirrored_diffs[n // 2] - mirrored_diffs[max(b, rc)] > 0
                )
                or (rd > b and mirrored_diffs[rd] - mirrored_diffs[b] > 0)
                or (a > rc and mirrored_diffs[a] - mirrored_diffs[rc] > 0)
            ):
                answer.append(False)
                continue

            left_range_count = subtract(counts[b], counts[a])
            right_range_count = subtract(counts[d], counts[c])

            if a > rd:
                right_range_count = subtract(
                    right_range_count, subtract(counts[min(a, rc)], counts[rd])
                )
            if rc > b:
                right_range_count = subtract(
                    right_range_count, subtract(counts[rc], counts[max(b, rd)])
                )
            if c > rb:
                left_range_count = subtract(
                    left_range_count, subtract(counts[min(c, ra)], counts[rb])
                )
            if ra > d:
                left_range_count = subtract(
                    left_range_count, subtract(counts[ra], counts[max(d, rb)])
                )

            answer.append(
                min(left_range_count) >= 0
                and min(right_range_count) >= 0
                and left_range_count == right_range_count
            )

        return answer

    def _get_mirrored_diffs(self, s: str) -> list[int]:
        diffs = [0]
        left, right = 0, len(s) - 1
        while left < right:
            diffs.append(diffs[-1] + (s[left] != s[right]))
            left += 1
            right -= 1
        return diffs

    def _get_counts(self, s: str) -> list[list[int]]:
        count = [0] * 26
        counts = [count.copy()]
        for char in s:
            count[ord(char) - ord("a")] += 1
            counts.append(count.copy())
        return counts


if __name__ == "__main__":
    test_cases = [
        (("abcabc", [[1, 1, 3, 5], [0, 2, 5, 5]]), [True, True]),
        (("abbcdecbba", [[0, 2, 7, 9]]), [False]),
        (("acbcab", [[1, 2, 4, 5]]), [True]),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().canMakePalindromeQueries(*args) == expected
