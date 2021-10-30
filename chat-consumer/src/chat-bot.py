from twitchio.ext import commands
from dynaconf import settings
from firebase import config


connection = config.connect()
class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=settings.TWITCH_TOKEN, client_id=settings.TWITCH_CLIENT_ID, nick='ROBOT_DEV', prefix='!',
                         initial_channels=['Gaules'])

    # Events don't need decorators when subclassed
    async def event_ready(self):
        print(f'Ready | {self.nick}')

    async def event_message(self, message):
        ref = connection.reference('/gaules')
        messages_ref = ref.child('messages')

        payload = {
          'id': str(message.id),
          'author': str(message.author.name),
          'content': str(message.content),
          'tags': str(message.tags),
        }

        messages_ref.push(payload)

        print(payload)

        await self.handle_commands(message)

    # Commands use a decorator...
    # @commands.command(name='test')
    # async def my_command(self, ctx):
    #     await ctx.send(f'Hello {ctx.author.name}!')


if __name__ == '__main__':
    bot = Bot()
    bot.run()
