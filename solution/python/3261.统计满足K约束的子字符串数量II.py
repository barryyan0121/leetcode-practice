from bisect import bisect_right


class Solution:
    def countKConstraintSubstrings(
        self, s: str, k: int, queries: list[list[int]]
    ) -> list[int]:
        leftmost = [0] * len(s)
        zeros = ones = left = 0
        for right, character in enumerate(s):
            if character == "0":
                zeros += 1
            else:
                ones += 1
            while zeros > k and ones > k:
                if s[left] == "0":
                    zeros -= 1
                else:
                    ones -= 1
                left += 1
            leftmost[right] = left

        prefix = [0]
        for right, start in enumerate(leftmost):
            prefix.append(prefix[-1] + right - start + 1)

        answer = []
        for query_left, query_right in queries:
            split = bisect_right(leftmost, query_left, query_left, query_right + 1)
            count = split - query_left
            total = count * (count + 1) // 2
            total += prefix[query_right + 1] - prefix[split]
            answer.append(total)
        return answer


if __name__ == "__main__":
    test_cases = [
        (("0001111", 2, [[0, 6]]), [26]),
        (("010101", 1, [[0, 5], [1, 4], [2, 3]]), [15, 9, 3]),
    ]
    for _, ((s, k, queries), expected) in enumerate(test_cases):
        assert Solution().countKConstraintSubstrings(s, k, queries) == expected
