from .. import Command

import random


@Command('/random')
def random_command(min_value=0, max_value=255, *args):
    number = random.randint(int(min_value), int(max_value))
    return 'Your lucky number is %s' % number
