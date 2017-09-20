from .. import Command
from ..abstractcommand import AbstractCommand


@Command('/echo')
class EchoCommand(AbstractCommand):

    @staticmethod
    def handle_command(*args):
        if args:
            out = ' '.join(args)
        else:
            out = 'I have nothing to say'
        return out
