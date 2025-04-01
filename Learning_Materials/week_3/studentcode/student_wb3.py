
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
        # SelectAndMoveFromOpenList()
        if len(self.open_list) == 0:
            return next_soln
        # my_index ← GetLastIndex(open_list)
        my_index = len(self.open_list) - 1

        # the_candidate ← open_list(my_index)
        next_soln = self.open_list[my_index]

        # RemoveFromOpenList(my_index)
        self.open_list.pop(my_index)


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
        if len(self.open_list) == 0:
            return next_soln
        # SelectAndMoveFromOpenList()
        # my_index ← GetFirstIndex(open_list)
        my_index = 0

        # the_candidate ← open_list(my_index)
        next_soln = self.open_list[my_index]

        # RemoveFromOpenList(my_index)
        self.open_list.pop(my_index)

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
        # Find the index of the candidate with the best quality in the openlist
        if self.open_list:
            best_quality = self.open_list[0].quality
            best_index = 0
            for i, candidate in enumerate(self.open_list):
                if candidate.quality < best_quality:
                    best_quality = candidate.quality
                    best_index = i

            # Remove the candidate with the best quality from the openlist
            next_soln = self.open_list.pop(best_index)


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
        if len(self.open_list) == 0:
            return next_soln

        # Find solution with minimum f(n) = g(n) + h(n)
        min_score = float('inf')
        min_index = 0

        for i, solution in enumerate(self.open_list):
            # Calculate f(n) = g(n) + h(n)
            # Using len(solution.variable_values) for path length and solution.quality for heuristic
            f_score = len(solution.variable_values) + solution.quality
            if f_score < min_score:
                min_score = f_score
                min_index = i

        # Get solution with minimum score and remove from openlist
        next_soln = self.open_list.pop(min_index)

        # <==== insert your pseudo-code and code above here
        return next_soln
wall_colour= 0.0
hole_colour = 1.0

def create_maze_breaks_depthfirst():
    # ====> insert your code below here
    #remember to comment out any mention of show_maze() before you submit your work

     # Load base maze
    maze = Maze(mazefile="maze.txt")

    maze.contents[3][4] = hole_colour  # Open path to trick DFS
    maze.contents[8][4] = wall_colour  # Block DFS at the end

    maze.contents[10][6] = hole_colour  # Another DFS trap
    maze.contents[14][6] = wall_colour  # Dead-end
    maze.contents[16][1] = hole_colour  # Dead-end
    maze.contents[19][4] = hole_colour  # Dead-end

    maze.contents[8][1] = hole_colour
    maze.contents[12][9] = wall_colour
    maze.contents[11][12] = wall_colour
    maze.contents[9][2] = wall_colour
    maze.contents[10][19] = wall_colour
    maze.contents[18][5] = wall_colour

    # Save the maze
    maze.save_to_txt("maze-breaks-depth.txt")

    # reload into new maze object
    print('this is the reloaded maze')
    reloaded_maze = Maze(mazefile="maze-breaks-depth.txt")

def create_maze_depth_better():
    # ====> insert your code below here
    #remember to comment out any mention of show_maze() before you submit your work

    # ====> insert your code below here
    #remember to comment out any mention of show_maze() before you submit your work
    maze = Maze(mazefile="maze.txt")
    maze.contents[1][8] = wall_colour
    maze.contents[9][10] = wall_colour
    maze.contents[15][6] = wall_colour
    maze.contents[13][2] = wall_colour
    maze.contents[12][13] = wall_colour
    maze.contents[2][13] = wall_colour
    maze.save_to_txt("maze-depth-better.txt")

    # <==== insert your code above here
