class Solution:
    def countMentions(self, numberOfUsers: int, events: list[list[str]]) -> list[int]:
        events.sort(key=lambda event: (int(event[1]), event[0][2]))
        answer = [0] * numberOfUsers
        online_until = [0] * numberOfUsers
        all_count = 0
        for event_type, timestamp, mentions in events:
            current = int(timestamp)
            if event_type[0] == "O":
                online_until[int(mentions)] = current + 60
            elif mentions[0] == "A":
                all_count += 1
            elif mentions[0] == "H":
                for user, until in enumerate(online_until):
                    if until <= current:
                        answer[user] += 1
            else:
                for mention in mentions.split():
                    answer[int(mention[2:])] += 1
        return [count + all_count for count in answer]


if __name__ == "__main__":
    test_cases = [
        ((2, [["MESSAGE", "10", "id1 id0"], ["OFFLINE", "11", "0"]]), [1, 1]),
    ]
    for _, ((number_of_users, events), expected) in enumerate(test_cases):
        assert Solution().countMentions(number_of_users, events) == expected
