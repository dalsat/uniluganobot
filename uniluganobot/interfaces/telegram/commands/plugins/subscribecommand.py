from .. import Command
from ..abstractcommand import AbstractCommand


@Command('/subscribe')
class SubscribeCommand(AbstractCommand):

    @classmethod
    def handle_command(cls, *args) -> str:
        return 'Sorry, I still have to learn to do that...'
