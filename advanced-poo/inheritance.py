class Person():

    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def hello(self):
        print('Hello!')

    def report(self):
        print(f'I am {self.first_name} {self.last_name}')


x = Person('Henrique', 'Al')
x.hello()
x.report ()

class Agent(Person):

    def __init__(self, first_name, last_name, code_name):
        Person.__init__(self, first_name, last_name)
        self.code_name = code_name

    def report(self):
        print('I am here')

    def reveal(self, passcode):
        if passcode == 123:
            print('I am a secret agent')
        else:
            self.report()

a = Agent('Xim', 'Xalabim', 'MrPepino')
a.reveal(12)