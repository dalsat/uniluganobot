from .defaultcommand import DefaultCommand


class Command:

    commands = {}
    _default_command = DefaultCommand()

    def __init__(self, command):
        self.command = command

    def __call__(self, handler):
        # print('registering %s as %s' % (handler.__name__, self.command))
        self.commands[self.command] = handler
        handler._command = self.command
        return handler

    @classmethod
    def named(cls, command):
        if command in cls.commands:
            return cls.commands[command]
        else:
            return cls._default_command

    @classmethod
    def execute_command(cls, command, *args):
        return cls.named(command).execute(*args)
