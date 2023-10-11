import unittest  #importing unittest library
from maze import Maze  #importing Maze class from maze

class Tests(unittest.TestCase):  #creating the Test class which will use methods to test different code cases
    def test_maze_create_cells(self):  #test case verifiying that the create_cells maze method functions as intended
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1.cells), num_cols)
        self.assertEqual(len(m1.cells[0]), num_rows)

    def test_maze_break_entrance_and_exit(self):  #test case verifying that the break_entrance_and_exit maze method functions as intended
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(m1.cells[0][0].has_top_wall, False)
        self.assertEqual(m1.cells[num_cols - 1][num_rows - 1].has_bottom_wall, False)

    def test_maze_reset_cells_visited(self):  #test case verifiying that the reset_cells_visited maze method functions as intended
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for j in range(0, num_cols):
            for i in range(0, num_rows):
                self.assertEqual(m1.cells[j][i].visited, False)

if __name__ == "__main__":  #Runs all test cases
    unittest.main()