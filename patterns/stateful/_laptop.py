from _off import Off
class Laptop:
    def __init__(self) -> None:
        self.state = Off()
    def change(self, change_to):
        self.state.switch(change_to)
