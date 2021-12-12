from generator.call_generator import Generator

"""
Main class that is used to initialize
a new instance of the Generator class,
the run method is called, when called
it finds the current instance, calls
the function for start_generator.
"""


class Main:

    def __init__(self):
        self.page = Generator()

    def run(self):
        self.page.start_generator()


main = Main()
main.run()
