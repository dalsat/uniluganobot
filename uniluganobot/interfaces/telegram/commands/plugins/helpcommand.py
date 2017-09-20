from .. import Command


@Command('/help')
class HelpCommand:

    def __call__(self, *args):
        out = 'Help!'
        return out
