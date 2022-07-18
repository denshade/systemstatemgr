import os
import time
import mlrose_hiive


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

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
def get_transitions_mlrose(states_to_visit, transitions):
    state_list = []
    dist_list = []
    for transition in transitions:
        if transition.from_state not in state_list:
            state_list.append(transition.from_state)
        if transition.to_state not in state_list:
            state_list.append(transition.to_state)

        dist_list.append(
            (state_list.index(transition.from_state), state_list.index(transition.to_state), transition.weight))
    fitness_dists = mlrose_hiive.TravellingSales(distances=dist_list)
    problem_fit = mlrose_hiive.TSPOpt(length=len(states_to_visit), fitness_fn=fitness_dists,
                                      maximize=False)
    state, best_fitness, other = mlrose_hiive.genetic_alg(problem_fit)
    return state.tolist()

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
                break

        if not found_transition:
            raise Exception(f"no transition found for {state_to_visit}")
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
