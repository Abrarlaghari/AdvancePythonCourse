class Sub():
    def __init__(self, publisher ) -> None:
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        pass
