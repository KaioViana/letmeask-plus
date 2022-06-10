class Integration:
    def __init__(self, client_id, token):
        self._client_id = client_id
        self._token = token
        self.validate()

    def validate(self):
        if len(self._client_id.strip()) == 0:
            raise Exception('client id required')

        if len(self._token.strip()) == 0:
            raise Exception('token required')

    def change_integration(self, client_id, token):
        if client_id == self._client_id:
            raise Exception('client_id already created')
        if token == self._token:
            raise Exception('token already created')

        return Integration(client_id, token)

    def get_integration_values(self):
        return {'client_id': self._client_id, 'token': self._token}
