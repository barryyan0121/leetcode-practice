"""1820. 最多邀请的个数"""


class Solution:
    def maximumInvitations(self, grid: list[list[int]]) -> int:
        matched = [-1] * len(grid[0])

        def visit(person: int, seen: set[int]) -> bool:
            for invitation, allowed in enumerate(grid[person]):
                if allowed and invitation not in seen:
                    seen.add(invitation)
                    if matched[invitation] == -1 or visit(matched[invitation], seen):
                        matched[invitation] = person
                        return True
            return False

        return sum(visit(person, set()) for person in range(len(grid)))


if __name__ == "__main__":
    test_cases = [
        (([[1, 1, 1], [1, 0, 1], [0, 0, 1]],), 3),
        (([[1, 0, 0], [0, 1, 0], [0, 0, 1]],), 3),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maximumInvitations(*args) == expected
