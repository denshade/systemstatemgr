import os
import json
import state
import sys

def load_from_file(state_file, transitions_file):
    f = open(state_file)
    print(f)
    states = json.load(f)
    resulting_states = []
    for json_state in states:
        resulting_states.append(state.State(json_state["state_name"], json_state["tests"]))
    f = open(transitions_file)
    resulting_transitions = []
    transitions = json.load(f)
    for json_transition in transitions:
        resulting_transitions.append(state.Transition(json_transition["from_state"],
                                                      json_transition["to_state"],
                                                      json_transition["script_to_run"], 0))
    return resulting_states, resulting_transitions

def run(states, transitions):
    for transition in transitions:
        from_state = transition.from_state
        to_state = transition.to_state
        print(f"{from_state} -> {to_state}")
        print(f"Running {transition.script_to_run}")
        os.system(transition.script_to_run)
        for current_state in states:
            if current_state.state_name == to_state:
                print(f"run tests {current_state.tests}")
                break


def load_and_run(state_file, transitions_file):
    print("Loading states and transitions")
    resulting_states, resulting_transitions = load_from_file(state_file, transitions_file)
    print("Done loading states and transitions")
    print("Running all transitions to get an estimate of timings")
    resulting_transitions = state.populate_transitions(resulting_transitions)
    print("Done running all transitions to get an estimate of timings")
    print("Searching for optimal transitions")
    sorted_transitions = state.try_random_transitions(resulting_states, resulting_transitions, 100)
    print("Done searching for optimal transitions")
    print(f"Starting to run {sorted_transitions}")
    run(resulting_states, sorted_transitions)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: state_file.json transition_files.json")
        sys.exit(2)

    load_and_run(sys.argv[1], sys.argv[2])