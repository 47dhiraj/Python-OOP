class _Private():                       # Class lai private garauna agadi pati single underscore (i.e _) lekhincha
    def __init__(self, name):
        self.name = name
        print('Hello', self.name)


class NotPrivate():                     # public class
    def __init__(self, name):
        self.name = name
        self.priv = _Private(name)

    def _display(self):                 # private method
        print("Hello", self.name)

    def display(self):
        print("Hi", self.name)


