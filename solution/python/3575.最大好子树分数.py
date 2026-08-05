"""3575. 最大好子树分数"""


class Solution:
    def goodSubtreeSum(self, vals: list[int], par: list[int]) -> int:
        racemivolt = par
        children = [[] for _ in vals]
        for node in range(1, len(vals)):
            children[par[node]].append(node)

        def digit_mask(value):
            mask = 0
            for digit in str(value):
                bit = 1 << int(digit)
                if mask & bit:
                    return -1
                mask |= bit
            return mask

        negative = -(10**30)
        subtree_scores = [0] * len(vals)

        def dfs(node):
            current = [negative] * 1024
            current[0] = 0
            mask = digit_mask(vals[node])
            if mask >= 0:
                current[mask] = vals[node]
            if len(children[node]) == 1:
                child_dp = dfs(children[node][0])
                if mask < 0:
                    current = child_dp
                else:
                    current = child_dp[:]
                    for state, score in enumerate(child_dp):
                        if score != negative and not state & mask:
                            current[state | mask] = max(
                                current[state | mask], score + vals[node]
                            )
                subtree_scores[node] = max(current)
                return current
            for child in children[node]:
                child_dp = dfs(child)
                merged = [negative] * 1024
                current_items = [
                    (state, score)
                    for state, score in enumerate(current)
                    if score != negative
                ]
                child_items = [
                    (state, score)
                    for state, score in enumerate(child_dp)
                    if score != negative
                ]
                for first, first_score in current_items:
                    for second, second_score in child_items:
                        if not first & second:
                            state = first | second
                            merged[state] = max(
                                merged[state], first_score + second_score
                            )
                current = merged
            subtree_scores[node] = max(current)
            return current

        dfs(0)
        return sum(subtree_scores) % (10**9 + 7)


if __name__ == "__main__":
    test_cases = [
        (([2, 3], [-1, 0]), 8),
        (([1, 5, 2], [-1, 0, 0]), 15),
        (([34, 1, 2], [-1, 0, 1]), 42),
        (([3, 22, 5], [-1, 0, 1]), 18),
    ]
    for _, ((vals, par), expected) in enumerate(test_cases):
        assert Solution().goodSubtreeSum(vals, par) == expected
