class Solution:
    def longestDecomposition(self, text: str) -> int:
        left = right = ""
        chunks = 0
        for index in range(len(text)):
            left += text[index]
            right = text[-index - 1] + right
            if left == right:
                chunks += 1
                left = right = ""
        return chunks


if __name__ == "__main__":
    test_cases = [
        ("ghiabcdefhelloadamhelloabcdefghi", 7),
        ("merchant", 1),
        ("antaprezatepzapreanta", 11),
        ("aaa", 3),
    ]
    for _, (text, expected) in enumerate(test_cases):
        assert Solution().longestDecomposition(text) == expected
