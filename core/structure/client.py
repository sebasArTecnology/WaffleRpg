import discord

from core.structure.utils import Utils
from core.structure.views import Views
from core.structure.commands import Commands

class Client(discord.Client):
    def __init__(self, **kargs):
        super().__init__()

        self.config: dict = kargs.get("config")
        self.main_path: str = kargs.get("main_path")
        self.database: object = kargs.get("database")

        self.utils = Utils(self)
        self.views = Views(self)
        self.commands = Commands(self)

    async def on_ready(self) -> None:
        print(f"@ Logged as {self.user}")

    async def on_message(self, message: object) -> None:
        if not message.author.bot and not self.utils.is_DMChannel(message):

            command, arguments = self.utils.is_Command(message)
            if command and command in self.commands.methods:

                if self.config["DebugMode"]:
                    print(f"User<{message.author}> : {message.content}")

                # Calls a command if it exist:
                await self.commands.methods[command](message, arguments)


