class Bot:
    def __init__(self, id, name, channel_consumer):
        self._id = id
        self._name = name
        self._channel_consumer = channel_consumer
        self.validate()

    def validate(self):
        if len(self._id) == 0:
            raise Exception('id is required')
        if len(self._name) == 0:
            raise Exception('name is required')
        if len(self._channel_consumer) == 0:
            raise Exception('channel consumer is required')
