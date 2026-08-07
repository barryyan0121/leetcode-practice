#
# @lc app=leetcode.cn id=642 lang=python3
#
# [642] 设计搜索自动补全系统
#


# @lc code=start
class AutocompleteSystem:
    def __init__(self, sentences, times):
        self.counts = dict(zip(sentences, times))
        self.current = ""

    def input(self, c: str):
        if c == "#":
            self.counts[self.current] = self.counts.get(self.current, 0) + 1
            self.current = ""
            return []
        self.current += c
        return sorted(
            (s for s in self.counts if s.startswith(self.current)),
            key=lambda s: (-self.counts[s], s),
        )[:3]


# @lc code=end


if __name__ == "__main__":
    system = AutocompleteSystem(
        ["i love you", "island", "ironman", "i love leetcode"], [5, 3, 2, 2]
    )
    assert system.input("i") == ["i love you", "island", "i love leetcode"]
    assert system.input("#") == []
