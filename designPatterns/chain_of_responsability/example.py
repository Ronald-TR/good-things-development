class Cat:
    def __init__(self):
        self.sucessor = None

    def execute_action(self, action):
        if action == 'meow':
            print('Cat is saying Meow! Meow!')
            return self

        if not self.sucessor:
            msg = f'Not sucessor for the {self.__class__.__name__} object'
            raise Exception(msg)

        self.sucessor.execute_action(action)

    def Responsability(self, sucessor):
        self.sucessor = sucessor
        return self


class Dog:
    def __init__(self):
        self.sucessor = None

    def execute_action(self, action):
        if action == 'rolf':
            print('Dog is saying Rolf! Rolf!')
            return self

        if not self.sucessor:
            msg = f'Not sucessor for the {self.__class__.__name__} object'
            raise Exception(msg)

        self.sucessor.execute_action(action)

    def Responsability(self, sucessor):
        self.sucessor = sucessor
        return self


class Elephant:
    def __init__(self):
        self.sucessor = None

    def execute_action(self, action):
        if action == 'dance':
            print('Elephant is dancing! dancing!')
            return self

        if not self.sucessor:
            msg = f'Not sucessor for the {self.__class__.__name__} object'
            raise Exception(msg)

        self.sucessor.execute_action(action)

    def Responsability(self, sucessor):
        self.sucessor = sucessor
        return self


c = Cat().Responsability(Dog().Responsability(Elephant().Responsability(None)))
c.execute_action('dance')
