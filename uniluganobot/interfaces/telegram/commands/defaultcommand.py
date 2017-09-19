import random
from .abstractcommand import AbstractCommand


class DefaultCommand(AbstractCommand):

    command = 'default'

    answers = [
        "I don't understand",
        "I'm not sure I got it",
        "Try in your own words",
        "Not a chance",
        "Wait, did you mean...?\nOh, nevermind",
        "I'm sorry, it's not you, it's me"
    ]

    @classmethod
    def handle_command(cls, *args):
        return random.choice(cls.answers)
