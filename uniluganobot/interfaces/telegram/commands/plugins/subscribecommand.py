from .. import Command
from ..abstractcommand import AbstractCommand


@Command.register
class SubscribeCommand(AbstractCommand):

    command = '/subscribe'

    @classmethod
    def handle_command(cls, *args) -> str:
        return 'Sorry, I still have to learn to do that...'
