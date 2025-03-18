
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
        if self.openlist:
            best_index = 0
            best_quality = self.openlist[0].quality

            for i in range(1, len(self.openlist)):
                if self.openlist[i].quality > best_quality:
                    best_quality = self.openlist[i].quality
                    best_index = i

            # Remove the best candidate from the openlist and return it
            next_soln = self.openlist.pop(best_index)

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
        # Find the index of the candidate with the best quality in the openlist
        best_index = 0
        best_quality = float('inf')
        for i, candidate in enumerate(self.open_list):
            if candidate.quality + len(candidate) < best_quality:
                best_quality = candidate.quality + len(candidate)
                best_index = i
        # Get the candidate with the best quality from the openlist
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
        # Find the index of the candidate with the best quality in the openlist
        if self.openlist:
            best_index = 0
            # A* score = path cost (length) + heuristic (quality)
            best_score = self.openlist[0].length + self.openlist[0].quality

            for i in range(1, len(self.openlist)):
                current_score = self.openlist[i].length + self.openlist[i].quality
                if current_score < best_score:
                    best_score = current_score
                    best_index = i

            # Remove the best candidate from the openlist and return it
            next_soln = self.openlist.pop(best_index)

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
        # Find the index of the candidate with the best quality in the openlist
        best_index = 0
        best_quality = float('inf')
        for i, candidate in enumerate(self.open_list):
            if candidate.quality + len(candidate) < best_quality:
                best_quality = candidate.quality + len(candidate)
                best_index = i
                # Get the candidate with the best quality from the openlist
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
            # Find the index of the candidate with the lowest combined score in the openlist
        if self.openlist:
            best_index = 0
            # A* score = path cost (length) + heuristic (quality)
            best_score = self.openlist[0].length + self.openlist[0].quality

            for i in range(1, len(self.openlist)):
                current_score = self.openlist[i].length + self.openlist[i].quality
                if current_score < best_score:
                    best_score = current_score
                    best_index = i

            # Remove the best candidate from the openlist and return it
            next_soln = self.openlist.pop(best_index)

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
        # Find the index of the candidate with the lowest combined score in the open_list
        if self.open_list:  # Note: using open_list instead of openlist
            best_index = 0
            # A* score = path cost (length) + heuristic (quality)
            best_score = self.open_list[0].length + self.open_list[0].quality

            for i in range(1, len(self.open_list)):
                current_score = self.open_list[i].length + self.open_list[i].quality
                if current_score < best_score:
                    best_score = current_score
                    best_index = i

            # Remove the best candidate from the open_list and return it
            next_soln = self.open_list.pop(best_index)

        # <==== insert your pseudo-code and code above here
        return next_soln
