from _computer_state import ComputerState
class Off(ComputerState):
    name = 'Off' # only class property and called by instances
    allowed = ['On']
