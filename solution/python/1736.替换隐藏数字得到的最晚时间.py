class Solution:
    def maximumTime(self, time: str) -> str:
        chars = list(time)
        if chars[0] == "?":
            chars[0] = "2" if chars[1] in "?0123" else "1"
        if chars[1] == "?":
            chars[1] = "3" if chars[0] == "2" else "9"
        if chars[3] == "?":
            chars[3] = "5"
        if chars[4] == "?":
            chars[4] = "9"
        return "".join(chars).replace("?", "9")


if __name__ == "__main__":
    solution = Solution()
    assert solution.maximumTime("2?:?0") == "23:50"
    assert solution.maximumTime("0?:3?") == "09:39"
    assert solution.maximumTime("1?:22") == "19:22"
    print("1736 passed")
