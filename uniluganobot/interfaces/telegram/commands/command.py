from .defaultcommand import DefaultCommand


class Command:

    commands = {}
    _default_command = DefaultCommand()

    @classmethod
    def register_command(cls, command: str, handler_class):
        print('registering command %s as %s' % (handler_class.__name__, command))
        cls.commands[command] = handler_class

    @classmethod
    def command_named(cls, command):
        if command in cls.commands:
            return cls.commands[command]
        else:
            return cls._default_command

    @classmethod
    def register(cls, handler_class):
        cls.register_command(handler_class.command, handler_class)

        def new_callable(*args):
            return handler_class(*args)
        return new_callable

    @classmethod
    def execute_command(cls, command, *args):
        return cls.command_named(command).execute(*args)
