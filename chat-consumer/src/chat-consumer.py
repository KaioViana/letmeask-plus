from twitchio.ext import commands
from dynaconf import settings
from firebase import config
from mongo.config import connect
from datetime import datetime


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=settings.TWITCH_TOKEN, client_id=settings.TWITCH_CLIENT_ID, nick='ROBOT_DEV', prefix='!',
                         initial_channels=['Gaules'])

        self.connection_firebase = config.connect() # connect firebase
        self.ref = self.connection_firebase.reference('/gaules')
        self.messages_ref = self.ref.child('messages')

        self.mongo = connect() # connect mongo
        self.messages_collection = self.mongo['gaules']
        self.count = 0  # temp count


    # Events don't need decorators when subclassed
    async def event_ready(self):
        print(f'Ready | {self.nick}')

    async def event_message(self, message):
        with open('count.txt', 'w') as file:
            self.count += 1
            file.write(str(self.count))

        payload = {
          'id': str(message.id),
          'author': str(message.author.name),
          'content': str(message.content),
          'tags': message.tags,
          'created_at': datetime.utcnow()
        }

        self.messages_ref.push(payload)
        self.messages_collection.insert_one(payload)

        await self.handle_commands(message)


    # NÃO VAMOS USAR POR AGORA

    # Commands use a decorator...
    # @commands.command(name='test')
    # async def my_command(self, ctx):
    #     await ctx.send(f'Hello {ctx.author.name}!')


if __name__ == '__main__':
    bot = Bot()
    bot.run()
