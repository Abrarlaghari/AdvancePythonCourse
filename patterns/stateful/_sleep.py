from _computer_state import ComputerState
class Sleep(ComputerState):
    name = 'Sleep' # only class property and called by instances
    allowed = ['On', 'Hybernate']
