import os
import time


class State:
    def __init__(self, state_name, tests, required_state):
        self.state_name = state_name
        self.tests = tests
        self.required_state = required_state


class Transition:
    def __init__(self, from_state, to_state, script_to_run, weight):
        self.script_to_run = script_to_run
        self.from_state = from_state
        self.weight = weight
        self.to_state = to_state


#
# Returns the used transitions.
def get_transitions(states_to_visit, transitions):
    resulting_transitions = []
    current_state = "START"
    for state_to_visit in states_to_visit:
        found_transition = False
        for transition in transitions:
            if transition.from_state == current_state and transition.to_state == state_to_visit:
                resulting_transitions.append(transition)
                found_transition = True
                current_state = state_to_visit
                break

        if not found_transition:
            raise Exception(f"no transition found for from {current_state} to {state_to_visit}")
    return resulting_transitions


#
# run the transitions.
def populate_transitions(transitions):
    for transition in transitions:
        t1_start = time.time()
        exitcode = os.system(transition.script_to_run)
        t1_stop = time.time()
        if exitcode != 0:
            raise Exception(f"{transition.script_to_run} failed with exit code: {exitcode}")
        transition.weight = t1_stop - t1_start
    return transitions
