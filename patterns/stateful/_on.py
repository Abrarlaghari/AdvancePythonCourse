from _computer_state import ComputerState
class On(ComputerState):
    name = 'On' # only class property and called by instances
    allowed = ['Off', 'Sleep', 'Hybernate']
