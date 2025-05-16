
from approvedimports import *

class DepthFirstSearch(SingleMemberSearch):
    """your implementation of depth first search to extend
    the superclass SingleMemberSearch search.
    Adds  a __str__method
    Over-rides the method select_and_move_from_openlist
    to implement the algorithm
    """

    def __str__(self):
        return "depth-first"

    def select_and_move_from_openlist(self) -> CandidateSolution:
        """void in superclass
        In sub-classes should implement different algorithms
        depending on what item it picks from self.open_list
        and what it then does to the openlist

        Returns
        -------
        next working candidate (solution) taken from openlist
        """

        # create a candidate solution variable to hold the next solution
        next_soln = CandidateSolution()

        # ====> insert your pseudo-code and code below here
        # check if open list is empty, return return None to avoid errors
        if len(self.open_list) == 0:
            return None
        # grab the last item from the list (like a stack, LIFO)
        next_soln = self.open_list[-1]
        # remove that item so we don't pick it again
        self.open_list.pop()


        # <==== insert your pseudo-code and code above here
        return next_soln

class BreadthFirstSearch(SingleMemberSearch):
    """your implementation of depth first search to extend
    the superclass SingleMemberSearch search.
    Adds  a __str__method
    Over-rides the method select_and_move_from_openlist
    to implement the algorithm
    """

    def __str__(self):
        return "breadth-first"

    def select_and_move_from_openlist(self) -> CandidateSolution:
        """Implements the breadth-first search algorithm

        Returns
        -------
        next working candidate (solution) taken from openlist
        """
        # create a candidate solution variable to hold the next solution
        next_soln = CandidateSolution()

        # ====> insert your pseudo-code and code below here
        # if the list is empty, return None to avoid errors
        if len(self.open_list) == 0:
            return None
        # take the first item from the list (like a queue, FIFO)
        next_soln = self.open_list[0]
        # remove it so we move on to the next one
        self.open_list.pop(0)

        # <==== insert your pseudo-code and code above here
        return next_soln

class BestFirstSearch(SingleMemberSearch):
    """Implementation of Best-First search."""

    def __str__(self):
        return "best-first"

    def select_and_move_from_openlist(self) -> CandidateSolution:
        """Implements Best First by finding, popping and returning member from openlist
        with best quality.

        Returns
        -------
        next working candidate (solution) taken from openlist
        """

        # create a candidate solution variable to hold the next solution
        next_soln = CandidateSolution()

        # ====> insert your pseudo-code and code below here
        # if the list is empty, return None to stop
        if len(self.open_list) == 0:
            return None
        # start with the first item as the best
        best_index = 0
        best_quality = self.open_list[0].quality
        # loop through the list to find the item with lowest quality (closest to goal)
        for i in range(len(self.open_list)):
            if self.open_list[i].quality < best_quality:
                best_index = i
                best_quality = self.open_list[i].quality
        # pick the best item
        next_soln = self.open_list[best_index]
        # remove it from the list
        self.open_list.pop(best_index)


        # <==== insert your pseudo-code and code above here
        return next_soln

class AStarSearch(SingleMemberSearch):
    """Implementation of A-Star  search."""

    def __str__(self):
        return "A Star"

    def select_and_move_from_openlist(self) -> CandidateSolution:
        """Implements A-Star by finding, popping and returning member from openlist
        with lowest combined length+quality.

        Returns
        -------
        next working candidate (solution) taken from openlist
        """

        # create a candidate solution variable to hold the next solution
        next_soln = CandidateSolution()

        # ====> insert your pseudo-code and code below here
        # if no items in list, return None to stop
        if len(self.open_list) == 0:
            return None
        # set up to find best score using index and solution
        best_index, best_score, next_soln = 0, float('inf'), None
        # loop through list to find lowest score (quality + moves)
        for i, sol in enumerate(self.open_list):
            score = sol.quality + len(sol.variable_values)
            # update if this score is better
            if score < best_score:
                best_index, best_score, next_soln = i, score, sol
        # pop the chosen item from list
        self.open_list.pop(best_index)

        # <==== insert your pseudo-code and code above here
        return next_soln
wall_colour= 0.0
hole_colour = 1.0

def create_maze_breaks_depthfirst():
    # ====> insert your code below here
    # remember to comment out any mention of show_maze() before you submit your work
    # start with the original maze
    maze = Maze(mazefile="maze.txt")
    # open path to lure depth-first into trap
    maze.contents[3][4] = hole_colour
    # block path to create dead-end for depth-first
    maze.contents[8][4] = wall_colour
    # open another path to keep depth-first busy
    maze.contents[10][6] = hole_colour
    # add wall to make another dead-end
    maze.contents[14][6] = wall_colour
    # open path for another depth-first trap
    maze.contents[16][1] = hole_colour
    # open path to extend dead-end
    maze.contents[19][4] = hole_colour
    # open path to create more branches for depth-first
    maze.contents[8][1] = hole_colour
    # block path to limit depth-first options
    maze.contents[12][9] = wall_colour
    # add wall to block alternative route
    maze.contents[11][12] = wall_colour
    # block path to keep depth-first trapped
    maze.contents[9][2] = wall_colour
    # add wall to prevent easy goal access
    maze.contents[10][19] = wall_colour
    # block path to create more dead-ends
    maze.contents[18][5] = wall_colour
    # save the modified maze to file
    maze.save_to_txt("maze-breaks-depth.txt")
    # test loading the saved maze
    print('this is the reloaded maze')
    reloaded_maze = Maze(mazefile="maze-breaks-depth.txt")
    # <==== insert your code above here

def create_maze_depth_better():
    # ====> insert your code below here
    #remember to comment out any mention of show_maze() before you submit your work
    # load the base maze to start
    maze = Maze(mazefile="maze.txt")
    # block path to guide depth-first to goal
    maze.contents[1][8] = wall_colour
    # add wall to steer depth-first efficiently
    maze.contents[9][10] = wall_colour
    # close path to avoid depth-first detours
    maze.contents[15][6] = wall_colour
    # block route to keep depth-first on track
    maze.contents[13][2] = wall_colour
    # add wall to limit breadth-first options
    maze.contents[12][13] = wall_colour
    # block path to favor depth-first route
    maze.contents[2][13] = wall_colour
    # save the new maze to file
    maze.save_to_txt("maze-depth-better.txt")
    # <==== insert your code above here
