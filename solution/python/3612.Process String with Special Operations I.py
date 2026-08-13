class Solution:
    def processString(self, s: str) -> str:
        res = []
        for ch in s:
            if "a" <= ch <= "z":
                res.append(ch)
            elif ch == "*":
                if res:
                    res.pop()
            elif ch == "#":
                res += res
            else:
                res.reverse()
        return "".join(res)


if __name__ == "__main__":
    s = Solution()
    assert s.processString("a#b%*") == "ba"
    assert s.processString("z*#") == ""
    print("3612 ok")
