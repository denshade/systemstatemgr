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
    def __init__(self, from_state, to_state, script_to_run, weight):
        self.script_to_run = script_to_run
        self.from_state = from_state
        self.weight = weight
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

