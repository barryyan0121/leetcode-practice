"""3860. 不同邮件组"""


class Solution:
    def uniqueEmailGroups(self, emails: list[str]) -> int:
        groups = set()
        for email in emails:
            local, domain = email.lower().split("@", 1)
            local = local.split("+", 1)[0].replace(".", "")
            groups.add(f"{local}@{domain}")
        return len(groups)


if __name__ == "__main__":
    test_cases = [
        (
            (
                [
                    "test.email+alex@leetcode.com",
                    "test.e.mail+bob.cathy@leetcode.com",
                    "testemail+david@lee.tcode.com",
                ],
            ),
            2,
        ),
        ((["A@B.com", "a@b.com", "ab+xy@b.com", "a.b@b.com"],), 2),
        ((["a.b+c.d+e@DoMain.com", "ab+xyz@domain.com", "ab@domain.com"],), 1),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().uniqueEmailGroups(*args) == expected
