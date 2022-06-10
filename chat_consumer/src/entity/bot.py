class Bot:
    def __init__(self, id, name, channel_consumer):
        self._id = id
        self._name = name
        self._channel_consumer = channel_consumer
        self._integration = None
        self._active = False
        self.validate()

    def validate(self):
        if len(self._id) == 0:
            raise Exception('id is required')
        if len(self._name) == 0:
            raise Exception('name is required')
        if len(self._channel_consumer) == 0:
            raise Exception('channel consumer is required')

    def activate(self):
        self._active = True
        return self._active

    def deactivate(self):
        self._active = False
        return self._active

    def is_active(self):
        return self._active

    @property
    def integration(self):
        return self._integration

    @integration.setter
    def integration(self, value):
        self._integration = value
        return self._integration

    @integration.getter
    def integration(self):
        if self._integration != None:
            return self._integration.get_integration_values()
