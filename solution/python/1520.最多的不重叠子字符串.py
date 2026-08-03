# @lc app=leetcode.cn id=1520 lang=python3


class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = {char: s.index(char) for char in set(s)}
        last = {char: s.rindex(char) for char in set(s)}
        intervals = []
        for char, start in first.items():
            end = start
            valid = True
            index = start
            while index <= end:
                current = s[index]
                if first[current] < start:
                    valid = False
                    break
                end = max(end, last[current])
                index += 1
            if valid:
                intervals.append((end, start))
        intervals.sort()
        result = []
        previous_end = -1
        for end, start in intervals:
            if start > previous_end:
                result.append(s[start : end + 1])
                previous_end = end
        return result


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.maxNumOfSubstrings, ("adefaddaccc",), ["e", "f", "ccc"])]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1520 题 "最多的不重叠子字符串" 所有测试用例通过')
