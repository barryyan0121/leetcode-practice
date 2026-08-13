"""2284. 最多单词数的发件人"""


class Solution:
    def largestWordCount(self, messages: list[str], senders: list[str]) -> str:
        counts = {}
        for message, sender in zip(messages, senders):
            counts[sender] = counts.get(sender, 0) + len(message.split())
        return max(counts, key=lambda sender: (counts[sender], sender))


if __name__ == "__main__":
    assert (
        Solution().largestWordCount(
            [
                "Hello userTwooo",
                "Hi userThree",
                "Wonderful day Alice",
                "Nice day userThree",
            ],
            ["Alice", "userTwo", "userThree", "userThree"],
        )
        == "userThree"
    )
