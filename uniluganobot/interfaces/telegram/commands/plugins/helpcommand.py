from ..command import Command


@Command('/help')
@Command.commandlist
class HelpCommand:
    '''This command'''

    def __call__(self, *args, session=None):
        lines = []
        lines.append('Try with the following commands:')
        # try:
        for name, command in self._command_list.items():
            lines.append('{} - {}'.format(name, command.__doc__))
        # except UndefinedContextError:
        #     lines.append('unable to retrieve context')

        return '\n'.join(lines)
