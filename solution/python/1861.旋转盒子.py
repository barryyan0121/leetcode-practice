from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for row in box:
            write = len(row) - 1
            for index in range(len(row) - 1, -1, -1):
                if row[index] == "*":
                    write = index - 1
                elif row[index] == "#":
                    row[index], row[write] = ".", "#"
                    write -= 1
        return [list(column) for column in zip(*box[::-1])]

if __name__ == "__main__":
    assert Solution().rotateTheBox([["#", ".", "*", "."]]) == [["."], ["#"], ["*"], ["."]]
