class Command:
    def __init__(self, i_params=None):
        self.params = i_params

    def run(self):
        return 'Should have implemented this'

    def ready_to_json(self):
        params = {"com": self.__class__.__name__, "params": self.params}
        return params
