from approvedimports import *

def exhaustive_search_4tumblers(puzzle: CombinationProblem) -> list:
    """simple brute-force search method that tries every combination until
    it finds the answer to a 4-digit combination lock puzzle.
    """

    # check that the lock has the expected number of digits
    assert puzzle.numdecisions == 4, "this code only works for 4 digits"

    # create an empty candidate solution
    my_attempt = CandidateSolution()

    # ====> insert your code below here
    # Iterate through all possible values for each of the 4 tumblers
    for digit1 in puzzle.value_set:  # First tumbler
        for digit2 in puzzle.value_set:  # Second tumbler
            for digit3 in puzzle.value_set:  # Third tumbler
                for digit4 in puzzle.value_set:  # Fourth tumbler
                    # Set the candidate solution with the current combination
                    my_attempt.variable_values = [digit1, digit2, digit3, digit4]

                    # Try evaluating the current combination
                    try:
                        result = puzzle.evaluate(my_attempt.variable_values)
                        # If the result is 1, this is the correct combination
                        if result == 1:
                            return my_attempt.variable_values
                    except ValueError as e:
                        # Handle invalid guesses (though unlikely with value_set)
                        print(f"Invalid guess: {e}")
                        continue


    # <==== insert your code above here

    # should never get here
    return [-1, -1, -1, -1]

def get_names(namearray: np.ndarray) -> list:
    family_names = []
    # ====> insert your code below here
    # Iterate over each row of the array
    for row in range(namearray.shape[0]):
        # Slice the last 6 characters of the current row
        family_name_array = namearray[row, -6:]
        # Join the characters into a single string
        family_name = "".join(family_name_array)
        # Append the string to the list of family names
        family_names.append(family_name)
    # <==== insert your code above here
    return family_names

def check_sudoku_array(attempt: np.ndarray) -> int:
    tests_passed = 0
    slices = []  # this will be a list of numpy arrays

    # ====> insert your code below here

    # Use assertions to check that the array has 2 dimensions each of size 9
    assert attempt.ndim == 2, "Input must be a 2D array"
    assert attempt.shape[0] == 9, "Array must have 9 rows"
    assert attempt.shape[1] == 9, "Array must have 9 columns"

    # Add all rows to the slices list
    for i in range(9):
        row = attempt[i, :]
        slices.append(row)

    # Add all columns to the slices list
    for j in range(9):
        col = attempt[:, j]
        slices.append(col)

    # Add all 9 3x3 sub-squares to slices
    for i in range(0, 9, 3):  # Step by 3 to cover rows 0-2, 3-5, 6-8
        for j in range(0, 9, 3):  # Step by 3 to cover columns 0-2, 3-5, 6-8
            sub_square = attempt[i:i+3, j:j+3]
            slices.append(sub_square)

    # Check each slice for 9 unique values
    for slice in slices:
        # Get unique values in the slice
        unique_values = np.unique(slice)
        # If there are exactly 9 unique values, increment tests_passed
        if len(unique_values) == 9:
            tests_passed += 1

    # <==== insert your code above here
    # return count of tests passed
    return tests_passed
