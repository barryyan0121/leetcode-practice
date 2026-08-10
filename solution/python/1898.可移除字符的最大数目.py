"""1898. 可移除字符的最大数目"""


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: list[int]) -> int:
        def is_subsequence(count: int) -> bool:
            removed = set(removable[:count])
            index = 0
            for pos, char in enumerate(s):
                if pos not in removed and index < len(p) and char == p[index]:
                    index += 1
            return index == len(p)

        left, right = 0, len(removable)
        while left <= right:
            middle = (left + right) // 2
            if is_subsequence(middle):
                left = middle + 1
            else:
                right = middle - 1
        return right


if __name__ == "__main__":
    assert Solution().maximumRemovals("abcacb", "ab", [3, 1, 0]) == 2
