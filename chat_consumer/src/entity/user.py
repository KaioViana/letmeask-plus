class User:
    def __init__(self, id, name, nickname, user_channel):
        self._id = id
        self._name = name
        self._nickname = nickname
        self._user_channel = user_channel
        self.validate()

    def validate(self):
        if len(self._id) == 0:
            raise Exception('id is required')
        if len(self._name) == 0:
            raise Exception('name is required')
        if len(self._nickname) == 0:
            raise Exception('nickname is required')
        if len(self._user_channel) == 0:
            raise Exception('user channel is required')

    def get_nickname(self):
        return self._nickname

    def get_user_channel(self):
        return self._user_channel
    
    def change_nickname(self, nickname):
        self._nickname = nickname
        self.validate()

    def change_user_channel(self, user_channel):
        self._user_channel = user_channel
        self.validate()

