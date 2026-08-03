# @lc app=leetcode.cn id=2953 lang=python3

from collections import deque


class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        answer = 0
        start = 0
        for end in range(1, len(word) + 1):
            if end == len(word) or abs(ord(word[end]) - ord(word[end - 1])) > 2:
                answer += self._count_segment(word, k, start, end)
                start = end
        return answer

    @staticmethod
    def _count_segment(word: str, k: int, start: int, end: int) -> int:
        answer = 0
        for distinct_target in range(1, 27):
            counts = [0] * 26
            previous_counts = [0] * 26
            occurrences = [deque() for _ in range(26)]
            left = previous_left = start
            distinct = previous_distinct = 0
            for right in range(start, end):
                char = ord(word[right]) - ord("a")
                if counts[char] == 0:
                    distinct += 1
                counts[char] += 1
                occurrences[char].append(right)
                if previous_counts[char] == 0:
                    previous_distinct += 1
                previous_counts[char] += 1
                while distinct > distinct_target:
                    old = ord(word[left]) - ord("a")
                    counts[old] -= 1
                    occurrences[old].popleft()
                    if counts[old] == 0:
                        distinct -= 1
                    left += 1
                while previous_distinct > distinct_target - 1:
                    old = ord(word[previous_left]) - ord("a")
                    previous_counts[old] -= 1
                    if previous_counts[old] == 0:
                        previous_distinct -= 1
                    previous_left += 1
                limit = end
                for values in occurrences:
                    if values:
                        if len(values) < k:
                            limit = -1
                            break
                        limit = min(limit, values[-k])
                upper = min(previous_left - 1, limit)
                if upper >= left:
                    answer += upper - left + 1
        return answer


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.countCompleteSubstrings, ("igigee", 2), 3),
        (solution.countCompleteSubstrings, ("aaab", 3), 1),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 2953 题 "统计完全子字符串" 所有测试用例通过')
