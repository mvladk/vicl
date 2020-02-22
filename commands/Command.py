
"""
Abstract base class for command, implements runnable interface
initiates required parameters for child classes

"""
class Command(object):
    def __init__(self, i_params):
        self.params = i_params
        self.__init_param_variables_for_child_classes()

    def __init_param_variables_for_child_classes(self):
        required_params = self.get_required_params()
        for key in required_params:
            if key in self.params:
                setattr(self, key, self.params[key])

    def get_required_params(self):
        return []  # 'Should have implemented this'

    def run(self):
        return 'Should have implemented this'

    def ready_to_json(self):
        params = {"com": self.__class__.__name__, "params": self.params}
        return params
