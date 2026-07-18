from threading import Semaphore, Thread


class FooBar:
    def __init__(self, n: int):
        self.n = n
        self.foo_turn = Semaphore(1)
        self.bar_turn = Semaphore(0)

    def foo(self, printFoo) -> None:
        for _ in range(self.n):
            self.foo_turn.acquire()
            printFoo()
            self.bar_turn.release()

    def bar(self, printBar) -> None:
        for _ in range(self.n):
            self.bar_turn.acquire()
            printBar()
            self.foo_turn.release()


if __name__ == "__main__":
    test_cases = [(1, "foobar"), (3, "foobarfoobarfoobar")]
    for _, (n, expected) in enumerate(test_cases):
        output = []
        foo_bar = FooBar(n)
        threads = [
            Thread(target=foo_bar.bar, args=(lambda: output.append("bar"),)),
            Thread(target=foo_bar.foo, args=(lambda: output.append("foo"),)),
        ]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        assert "".join(output) == expected
