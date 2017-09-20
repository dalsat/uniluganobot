from .defaultcommand import DefaultCommand
import inspect


class Command:

    commands = {}
    _default_command = DefaultCommand

    def __init__(self, command):
        self.command = command

    def __call__(self, handler):
        print('registering %s as %s' % (handler.__name__, self.command))
        self.commands[self.command] = handler
        handler._command = self.command
        return handler

    @classmethod
    def at(cls, command):
        if command in cls.commands:
            return cls.commands[command]
        else:
            return cls._default_command

    @classmethod
    def execute(cls, command, *args, session=None):
        # return cls.named(command).execute(*args)
        if session is not None and command in session:
            callable_command = session[command]
        else:
            callable_command = cls.at(command)
            if inspect.isclass(callable_command):
                callable_command = callable_command()
            if session is not None:
                session[command] = callable_command
        return callable_command(*args)
