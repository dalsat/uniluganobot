from ..command import Command


@Command('/test')
class TestCommand:

    def __init__(self):
        self.counter = 0

    def __call__(self, *args):
        self.counter += 1
        return('counter: %s' % self.counter)
