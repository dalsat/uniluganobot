from .. import Command

import random


@Command('/random')
def random_command(min=0, max=255, *args):
    number = random.randint(int(min), int(max))
    return 'Your lucky number is %s' % number
