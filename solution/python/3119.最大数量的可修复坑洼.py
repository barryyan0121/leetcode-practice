"""3119. 最大数量的可修复坑洼"""


class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:
        blocks = []
        index = 0
        while index < len(road):
            if road[index] == ".":
                index += 1
                continue
            end = index
            while end < len(road) and road[end] == "x":
                end += 1
            blocks.append(end - index)
            index = end
        answer = 0
        for length in sorted(blocks, reverse=True):
            fixed = min(length, max(0, budget - 1))
            if fixed == length:
                budget -= length + 1
            else:
                budget -= fixed + 1
            answer += fixed
            if fixed < length:
                break
        return answer


if __name__ == "__main__":
    test_cases = [(("..", 5), 0), (("..xxxxx", 4), 3), (("x.x.xxx...x", 14), 6)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maxPotholes(*args) == expected
