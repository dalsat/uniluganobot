from .. import Command
from ..abstractcommand import AbstractCommand

import random


@Command.register
class RandomCommand(AbstractCommand):

    command = '/random'

    @staticmethod
    def handle_command(min=0, max=255, *args):
        number = random.randint(int(min), int(max))
        return 'Your lucky number is %s' % number
