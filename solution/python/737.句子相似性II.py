#
# @lc app=leetcode.cn id=737 lang=python3
#
# [737] 句子相似性 II
#


# @lc code=start
class Solution:
    def areSentencesSimilarTwo(self, sentence1, sentence2, similarPairs) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        parent = {}

        def find(word):
            parent.setdefault(word, word)
            if parent[word] != word:
                parent[word] = find(parent[word])
            return parent[word]

        def union(left, right):
            left, right = find(left), find(right)
            if left != right:
                parent[right] = left

        for left, right in similarPairs:
            union(left, right)
        return all(
            find(left) == find(right) for left, right in zip(sentence1, sentence2)
        )


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    assert solution.areSentencesSimilarTwo(
        ["great", "acting", "skills"],
        ["fine", "drama", "talent"],
        [["great", "fine"], ["acting", "drama"], ["skills", "talent"]],
    )
