from sub import Sub

class EmailSubscriber(Sub):
    def __init__(self, publisher) -> None:
        super().__init__(publisher)
