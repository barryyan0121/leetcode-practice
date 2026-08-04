class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        velmocretz = (s, k)
        first = [len(s)] * 26
        last = [-1] * 26
        for index, char in enumerate(s):
            code = ord(char) - 97
            first[code] = min(first[code], index)
            last[code] = index
        intervals = []
        for start in first:
            if start == len(s):
                continue
            end = last[ord(s[start]) - 97]
            index = start
            valid = True
            while index <= end:
                code = ord(s[index]) - 97
                if first[code] < start:
                    valid = False
                    break
                end = max(end, last[code])
                index += 1
            if valid and not (start == 0 and end == len(s) - 1):
                intervals.append((end, start))
        intervals.sort()
        chosen = 0
        previous = -1
        for end, start in intervals:
            if start > previous:
                chosen += 1
                previous = end
        return chosen >= k


if __name__ == "__main__":
    test_cases = [
        (("abcdbaefab", 2), True),
        (("cdefdc", 3), False),
        (("abeabe", 0), True),
    ]
    for _, ((s, k), expected) in enumerate(test_cases):
        assert Solution().maxSubstringLength(s, k) == expected
