""" This Basic simulator is for learning the simulator interface.
It can be used in this case to find the center between two numbers.
"""
from __future__ import print_function
import bonsai
import sys
from bonsai.simulator import SimState
from random import randint

""" If you would like to debug your code add this back in.
def debug(*args):
    print(*args, file=sys.stderr)
"""


class BasicSimulator(bonsai.Simulator):
    """ A basic simulator class that takes in a move from the inkling file,
    and returns the state as a result of that move.
    """

    min = 0
    max = 2
    goal = 1

    def __init__(self):
        super(BasicSimulator, self).__init__()
        self.goal_count = 0
        self.value = randint(self.min, self.max)
        self.old_value = self.min

    def get_terminal(self):
        """ Restarts the simulation if the AI moved out of bounds.
        """
        if (self.value < self.min or self.value > self.max):
            # (self.value == self.goal and self.old_value == self.goal)):

            # debug("terminal")
            self.reset()
            return True
        else:
            return False

    def start(self):
        """ Start the episode by initializing value to a random number
        between the min and max.
        """
        # debug("start")
        self.goal_count = 0
        self.old_value = self.min
        self.value = randint(self.min, self.max)

    def stop(self):
        """ Stop is called after a training session is complete.
        This simple game requires no cleanup after training.
        """
        # debug("stop")
        pass

    def reset(self):
        """ Reset is called to reset simulator state before the next training session.
        """
        # debug("reset")
        self.goal_count = 0
        self.old_value = self.min
        self.value = randint(self.min, self.max)

    def advance(self, actions):
        """ Function to make a move based on output from the BRAIN as defined
        in the Inkling file.
        """
        # debug("advance", actions["delta"])
        self.value += actions["delta"]
        if self.value == self.goal:
            self.goal_count += 1

    def get_state(self):
        """ Gets the state of the simulator, whether it be a valid value or
        terminal ("game over") state.
        """
        # debug("get_state")
        # debug("state", self.value)
        self.old_value = self.value
        return SimState(state={"value": self.value},
                        is_terminal=self.get_terminal())

    def time_at_goal(self):
        """ Function to return how long the simulation has maintained the goal.
        """
        return self.goal_count

if __name__ == "__main__":
    base_args = bonsai.parse_base_arguments()
    sim = BasicSimulator()
    bonsai.run_with_url('find_the_center_sim', sim,
                        base_args.brain_url, base_args.access_key)
