import random


class DefaultCommand:

    _command = 'default'

    answers = [
        "I don't understand",
        "I'm not sure I got it",
        "Try in your own words",
        "Not a chance",
        "Wait, did you mean...?\nOh, nevermind",
        "I'm sorry, it's not you, it's me"
    ]

    def __call__(self, *args):
        return random.choice(self.answers)
