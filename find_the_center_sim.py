""" This Basic simulator is for learning the simulator interface.
It can be used in this case to find the center between two numbers.
"""
import bonsai
import sys
from bonsai.simulator import SimState
from random import randint

#def debug(*args):
    #print(*args, file=sys.stderr)

class BasicSimulator(bonsai.Simulator):
    """ A basic simulator class that takes in a move from the inkling file, and returns the state as a result of that move.
    """
    min = 0
    max = 2
    goal = 1

    def __init__(self):
        super(self.__class__, self).__init__()
        self.goal_count = 0
        self.value = randint(self.min, self.max)
        self.old_value = self.min

    def get_terminal(self):
        """ Function to restart the simulation if the Inkling move was out of bounds.
        """
        if (self.value < self.min or
            self.value > self.max): # or
            #(self.value == self.goal and self.old_value == self.goal)):

            #debug("terminal")
            self.reset()
            return True
        else:
            return False

    def start(self):
        """ Function to start the episode by guessing a random integer between the min and max.
        """
        #debug("start")
        self.goal_count = 0
        self.old_value = self.min
        self.value = randint(self.min, self.max)

    def stop(self):
        """ Function to stop the simulator.
        """
        #debug("stop")
        pass

    def reset(self):
        """ Function to reset the simulation variables.
        """
        #debug("reset")
        self.goal_count = 0
        self.old_value = self.min
        self.value = randint(self.min, self.max)

    def advance(self, actions):
        """ Function to make a move based on input from Inkling file and if in the center,
        increases the total goal count by 1.
        """
        #debug("advance", actions["delta"])
        self.value += actions["delta"]
        if self.value == self.goal:
            self.goal_count += 1

    def get_state(self):
        """ Gets the state of the simulator, whether it be a valid value or terminal.
        """
        #debug("get_state")
        #debug("state", self.value)
        self.old_value = self.value
        return SimState(state={"value": self.value},is_terminal=self.get_terminal())

    def distance_from_goal(self):
        """ Function to determine how far away the move is from the center.
        """
        dist = abs(self.goal - self.value)
        #debug("dist", dist)
        return -1*dist

    def time_at_goal(self):
        """ Function to return how long the simulation has maintained the goal.
        """
        return self.goal_count

if __name__ == "__main__":
    base_args = bonsai.parse_base_arguments()
    sim = BasicSimulator()
    bonsai.run_with_url('find_the_center_sim', sim, base_args.brain_url, base_args.access_key)