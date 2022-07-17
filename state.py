# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class State:
    def __init__(self, state_name, tests, conflicting_state, required_state):
        self.state_name = state_name
        self.tests = tests
        self.conflicting_state = conflicting_state
        self.required_state = required_state


class Transition:
    def __init__(self, from_states, to_state, script_to_run):
        self.script_to_run = script_to_run
        self.from_states = from_states
        self.to_state = to_state

#
# A series of expected states sequences is given. e.g. [[state1], [state2, state3]]
# Returns the used transitions.
def get_plan(expected_states_sequence, available_states, transitions):
    picked_transitions = []
    for state_name in expected_states_sequence:
        for transition in transitions:
            if transition.to_state == state_name:
                picked_transitions.append(transition)

    return picked_transitions


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
