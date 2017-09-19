import abc


class AbstractCommand(abc.ABC):

    command = None

    @classmethod
    def execute(cls, *args) -> str:
        # cls.log(*args)
        return cls.handle_command(*args)

    @abc.abstractmethod
    def handle_command(cls, *args) -> str:
        "Override this to define the command behavior"

    @classmethod
    def log(cls, *args):
        print('[{}] {}'.format(cls.command, ' '.join(args)))
