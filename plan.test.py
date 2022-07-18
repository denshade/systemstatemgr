import unittest
from state import get_transitions
from state import Transition, populate_transitions

class TestStringMethods(unittest.TestCase):

    def test_plan_not_empty_for_one_state(self):
        transition1 = Transition("START", "init", "script1.sh", 12)
        transition2 = Transition("init", "START", "script2.sh", 12)

        first_transition = get_transitions(["init"], [transition1, transition2])[0]
        self.assertEqual(first_transition.from_state, "START")
        self.assertEqual(first_transition.to_state, "init")
        self.assertEqual(first_transition.script_to_run, "script1.sh")

    def test_plan_second_state(self):
        transition1 = Transition("START", "init", "script1.sh", 10)
        transition2 = Transition("START", "second", "script2.sh", 12)
        first_transition = get_transitions({"second"}, [transition1, transition2])[0]
        self.assertEqual(first_transition.from_state, "START")
        self.assertEqual(first_transition.to_state, "second")
        self.assertEqual(first_transition.script_to_run, "script2.sh")

    def test_plan_second_state_multiple(self):
        transition1 = Transition("START", "init", "script1.sh", 10)
        transition2 = Transition("START", "second", "script2.sh", 12)
        transition3 = Transition("second", "init", "script1-2.sh", 2)
        transitions = get_transitions({"init", "second"}, [transition1, transition2, transition3])
        first_transition = transitions[0]
        self.assertEqual(first_transition.from_state, "START")
        self.assertEqual(first_transition.to_state, "second")
        self.assertEqual(first_transition.script_to_run, "script2.sh")
        second_transition = transitions[1]
        self.assertEqual(second_transition.from_state, "second")
        self.assertEqual(second_transition.to_state, "init")
        self.assertEqual(second_transition.script_to_run, "script1-2.sh")


    def skipped_test_check_populate(self):
        transition1 = Transition("START", "init", "python3 sleep.py", 10)
        transitions = populate_transitions([transition1])
        self.assertIsNotNone(transitions[0].weight)

if __name__ == '__main__':
    unittest.main()