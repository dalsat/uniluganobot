import inspect

from .defaultcommand import DefaultCommand


class Command:

    commands = {}
    _default_command = DefaultCommand

    def __init__(self, command):
        self.command = command

    def __call__(self, handler):
        print('registering %s as %s' % (handler.__name__, self.command))
        self.commands[self.command] = handler
        handler._command = self.command
        if isinstance(handler, ContextCommand):
            print('setting context for %s' % self.command)
            handler.context = self
        return handler

    @classmethod
    def commandlist(cls, handler):
        handler._command_list = cls.commands
        return handler

    @classmethod
    def at(cls, command):
        if command in cls.commands:
            return cls.commands[command]
        else:
            return cls._default_command

    @staticmethod
    def getcallable(class_or_function):
        if inspect.isclass(class_or_function):
            class_or_function = class_or_function()
        return class_or_function

    @classmethod
    def execute(cls, command, *args, session=None):
        # return cls.named(command).execute(*args)
        if session is not None and command in session:
            callable_command = session[command]
        else:
            callable_command = cls.getcallable(cls.at(command))
            if session is not None:
                session[command] = callable_command
        return callable_command(*args)


class ContextCommand:

    def __init__(self):
        self._context = None

    @property
    def context(self):
        if self._context is None:
            raise UndefinedContextError
        else:
            return self._context

    @context.setter
    def context(self, context):
        self._context = context


class UndefinedContextError(Exception):
    pass
