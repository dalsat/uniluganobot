from .. import Command
from ..abstractcommand import AbstractCommand


@Command('/start')
class StartCommand(AbstractCommand):

    @staticmethod
    def handle_command(*args):
        out = '''
Hello and welcome to the UniLuganoBot.
Currently, UniLuganoBot provides general information about the daily
mensa menu. Try the command /mensa to see today's menu.

This is an unofficial bot, and it is not affiliated with
the university of Lugano
        '''
        return out
