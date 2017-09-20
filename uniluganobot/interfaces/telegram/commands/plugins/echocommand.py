from .. import Command


# @Command('/echo')
# class EchoCommand:
#
#     def __call__(self, *args):
#         if args:
#             out = ' '.join(args)
#         else:
#             out = 'I have nothing to say'
#         return out

@Command('/echo')
def echo_command(*args):
    if args:
        out = ' '.join(args)
    else:
        out = 'I have nothing to say'
    return out
