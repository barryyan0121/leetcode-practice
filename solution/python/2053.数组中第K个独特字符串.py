"""2053. 数组中第 K 个独特字符串"""


class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        counts = {word: arr.count(word) for word in arr}
        for word in arr:
            if counts[word] == 1:
                k -= 1
                if k == 0:
                    return word
        return ""


if __name__ == "__main__":
    test_cases = [((["d", "b", "c", "b", "c", "a"], 2), "a")]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().kthDistinct(*args) == expected
