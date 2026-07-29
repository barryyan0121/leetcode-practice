from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        answer = []
        for path in sorted(folder):
            if not answer or not path.startswith(answer[-1] + "/"):
                answer.append(path)
        return answer


if __name__ == "__main__":
    test_cases = [
        (["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"], ["/a", "/c/d", "/c/f"]),
        (["/a", "/a/b/c", "/a/b/d"], ["/a"]),
    ]
    for _, (folder, expected) in enumerate(test_cases):
        assert Solution().removeSubfolders(folder) == expected
