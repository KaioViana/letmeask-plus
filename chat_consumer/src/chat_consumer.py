from twitchio.ext import commands
from dynaconf import settings
from infra import firebase_config

# from mongo.config import connect
from datetime import datetime


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=settings.TWITCH_TOKEN, client_id=settings.TWITCH_CLIENT_ID, nick='ROBOT_DEV', prefix='!',
                         initial_channels=['Gaules'])

        self.connection_firebase = firebase_config.connect()  # connect firebase
        self.ref = self.connection_firebase.reference('/gaules')
        self.messages_ref = self.ref.child('messages')

        # self.mongo = connect() # connect mongo
        # self.messages_collection = self.mongo['gaules']

    # Events don't need decorators when subclassed

    async def event_ready(self):
        print(f'Ready | {self.nick}')

    async def event_message(self, message):
        payload = {
            'id': str(message.id),
            'author': str(message.author.name),
            'content': str(message.content),
            'tags': message.tags,
            'created_at': str(datetime.utcnow())
        }

        # self.messages_ref.push(payload) -> NÃO NECESSÁRIO POR AGORA
        print(payload)
        # self.messages_collection.insert_one(payload)

        await self.handle_commands(message)

    # NÃO VAMOS USAR POR AGORA

    # Commands use a decorator...
    # @commands.command(name='test')
    # async def my_command(self, ctx):
    #     await ctx.send(f'Hello {ctx.author.name}!')


if __name__ == '__main__':
    bot = Bot()
    bot.run()
