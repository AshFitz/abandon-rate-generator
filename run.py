from generator.run import Generator

class Main:
    """
    Constructor for class main.
    """
    def __init__(self):
        self.page = Generator()

    def run(self):
        self.page.start_generator()
        self.page.get_inbound_calls()
        self.page.get_dropped_calls()


main = Main()
main.run()
