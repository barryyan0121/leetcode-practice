"""2284. 最多单词数的发件人"""


class Solution:
    def largestWordCount(self, messages: list[str], senders: list[str]) -> str:
        counts = {}
        for message, sender in zip(messages, senders):
            counts[sender] = counts.get(sender, 0) + len(message.split())
        return max(counts, key=lambda sender: (counts[sender], sender))
