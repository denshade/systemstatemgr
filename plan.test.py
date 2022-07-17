import unittest
from state import get_plan
from state import State, Transition


class TestStringMethods(unittest.TestCase):

    def test_plan_not_empty_for_one_state(self):
        init = State("init", None, None, None)
        transition1 = Transition(["START"], "init", "script1.sh")
        first_transition = get_plan(["init"], [init], [transition1])[0]
        self.assertEqual(first_transition.from_states, ["START"])
        self.assertEqual(first_transition.to_state, "init")
        self.assertEqual(first_transition.script_to_run, "script1.sh")

    def test_plan_second_state(self):
        init = State("init", None, None, None)
        second = State("second", None, None, None)
        transition1 = Transition(["START"], "init", "script1.sh")
        transition2 = Transition(["START"], "second", "script2.sh")
        first_transition = get_plan(["second"], [init, second], [transition1, transition2])[0]
        self.assertEqual(first_transition.from_states, ["START"])
        self.assertEqual(first_transition.to_state, "second")
        self.assertEqual(first_transition.script_to_run, "script2.sh")

if __name__ == '__main__':
    unittest.main()