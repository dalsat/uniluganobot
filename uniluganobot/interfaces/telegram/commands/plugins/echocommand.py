from .. import Command
from ..abstractcommand import AbstractCommand


@Command.register
class EchoCommand(AbstractCommand):

    command = '/echo'

    @staticmethod
    def handle_command(*args):
        if args:
            out = ' '.join(args)
        else:
            out = 'I have nothing to say'
        return out
