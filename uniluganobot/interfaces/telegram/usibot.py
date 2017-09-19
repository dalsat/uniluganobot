import asyncio
import telepot
from telepot.aio.loop import MessageLoop
from telepot.aio.delegate import per_chat_id, create_open, pave_event_space
import os

# from . import botconfig
from .commands import Command


class UsiBot(telepot.aio.helper.ChatHandler):

    timeout = 10

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    def data_from(self, datasource: str) -> dict:
        if datasource in self.commands:
            return self.commands[datasource].data()

    async def on_chat_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)

        if content_type != 'text':
            response = "Nope, I don't do that kind of stuff..."
            await self.sender.sendMessage(response)
            return

        self.log(msg)
        command, *args = msg['text'].strip().lower().split()

        response = self.handle_command(command, *args)
        await self.sender.sendMessage(response, parse_mode='Markdown')

    def handle_command(self, command, *args):
        return Command.execute_command(command, *args)

    @classmethod
    def on_close(cls, event):
        pass

    @staticmethod
    def log(message):
        fields = [
            str(message['chat']['id']),
            message['chat']['first_name'],
            message['chat']['last_name'],
            message['chat']['username'],
            message['text']
        ]
        print('"{}","{}","{}","{}","{}"'.format(*fields))

    @classmethod
    def run(cls):

        token = os.environ['token']
        # token = botconfig.token()

        bot = telepot.aio.DelegatorBot(token, [
            pave_event_space()(
                per_chat_id(), create_open, cls, timeout=cls.timeout),
        ])

        loop = asyncio.get_event_loop()
        loop.create_task(MessageLoop(bot).run_forever())
        print('Listening ...')

        loop.run_forever()
