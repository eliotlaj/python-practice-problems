def is_target(grid, target):
    for row in grid:
        count = 0
        for n in row:
            if n == target:
                count += 1
        if count == 0:
            return False
    return True

def create_columns(grid):
    columns = []
    column_index = 0
    for i in range(len(grid[0])):
        new_column = []
        for row in grid:
            new_column.append(row[column_index])
        column_index += 1
        columns.append(new_column)
    return columns


def rows_and_columns_contain(lst, target):
    """
    Determines whether every row and every column of a list
      of lists contains a target value
    lst (list of lists): the list of lists
    target: the target value
    Returns: True if every row and every column of lst contains
      target, False otherwise
    """

    total_list = [lst + create_columns[list]]
    return is_target(total_list)


#############################################################
###                                                       ###
###                    Testing code.                      ###
###    !!! DO NOT MODIFY ANY CODE BELOW THIS POINT !!!    ###
###                                                       ###
#############################################################

import sys
sys.path.append('../')

import test_utils as utils


def do_test_rows_and_columns_contain(grid, target, expected):
    recreate_msg = "  grid = {}\n".format(grid)
    recreate_msg += utils.gen_recreate_msg("rows_and_columns_contain", *("grid", target))

    actual = rows_and_columns_contain(grid, target)

    utils.check_none(actual, recreate_msg)
    utils.check_type(actual, expected, recreate_msg)
    utils.check_equals(actual, expected, recreate_msg)


def test_rows_and_columns_contain_1():
    grid = [[1, 2], [3, 1]]
    do_test_rows_and_columns_contain(grid=grid, target=1, expected=True)


def test_rows_and_columns_contain_2():
    grid = [[1, 2], [3, 1]]
    do_test_rows_and_columns_contain(grid=grid, target=2, expected=False)


def test_rows_and_columns_contain_3():
    grid = [[1, 2], [3, 2]]
    do_test_rows_and_columns_contain(grid=grid, target=2, expected=False)


def test_rows_and_columns_contain_4():
    grid = [[2, 1, 2], [1, 3, 1], [2, 2, 3]]
    do_test_rows_and_columns_contain(grid=grid, target=2, expected=False)


def test_rows_and_columns_contain_5():
    grid = [[3, 1, 2], [1, 3, 1], [2, 2, 3]]
    do_test_rows_and_columns_contain(grid=grid, target=3, expected=True)

def test_rows_and_columns_contain_6():
    grid = [[2, 1, 1], [3, 2, 3], [2, 1, 3]]
    do_test_rows_and_columns_contain(grid=grid, target=2, expected=False)


def test_rows_and_columns_contain_7():
    grid = [[2, 1, 1], [1, 2, 3], [2, 1, 3]]
    do_test_rows_and_columns_contain(grid=grid, target=1, expected=True)


grid0 = [[2, 1, 1, 2],
         [1, 2, 3, 1],
         [3, 3, 1, 2],
         [1, 2, 1, 3]]

def test_rows_and_columns_contain_8():
    do_test_rows_and_columns_contain(grid=grid0, target=1, expected=True)


def test_rows_and_columns_contain_9():
    do_test_rows_and_columns_contain(grid=grid0, target=2, expected=False)


def test_rows_and_columns_contain_10():
    do_test_rows_and_columns_contain(grid=grid0, target=3, expected=False)


def test_rows_and_columns_contain_11():
    grid = [[1, 2], [3, 1], [1, 3]]
    do_test_rows_and_columns_contain(grid=grid, target=1, expected=True)


def test_rows_and_columns_contain_12():
    grid = [[1, 2], [3, 1], [1, 3]]
    do_test_rows_and_columns_contain(grid=grid, target=3, expected=False)
