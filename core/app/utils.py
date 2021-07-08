from core.app.models import User

class RpgManager:
    def __init__(self, database: object):
        self.database = database

    def is_user_exist(self, account_id: int) -> object:
        return self.database.query(User, User.account_id == str(account_id)).first()

    def create_user(self, account_id: int):
        self.database.insert(User(account_id = str(account_id)))
        self.database.commit()