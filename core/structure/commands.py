from core.app.utils import RpgManager

class Commands:
    """
     # --- # Glosario # --- #
    methods: object -> It's a dict with the name and
    what method it'll call for each command.
    """
    def __init__(self, client: object):
        self.manager = RpgManager(client.database)
        self.views = client.views
        self.methods = {
            "start": self.create_user
        }
    
    async def create_user(self, message : str, arguments : list) -> None:
        account: object = message.author

        if not self.manager.is_user_exist(account.id):
            self.manager.create_user(account.id)

        embed = self.views.show_profile(account)
        await message.channel.send(embed = embed)