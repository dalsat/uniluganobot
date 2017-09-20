from .. import Command
from ..abstractcommand import AbstractCommand

import random


@Command('/random')
class RandomCommand(AbstractCommand):

    @staticmethod
    def handle_command(min=0, max=255, *args):
        number = random.randint(int(min), int(max))
        return 'Your lucky number is %s' % number
