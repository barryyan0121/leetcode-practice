"""2301. 替换字符后匹配"""


class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: list[list[str]]) -> bool:
        allowed = {}
        for source, target in mappings:
            allowed.setdefault(source, set()).add(target)
        for i in range(len(s) - len(sub) + 1):
            if all(a == b or a in allowed.get(b, set()) for a, b in zip(s[i:], sub)):
                return True
        return False


if __name__ == "__main__":
    assert Solution().matchReplacement(
        "fool3e7bar", "leet", [["e", "3"], ["t", "7"], ["t", "8"]]
    )
