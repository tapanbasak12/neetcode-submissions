class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict=defaultdict(set)
        column_dict=defaultdict(set)
        square_dict=defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[i])):
                element = board[i][j]
                if element == ".":
                    continue
                if (element in row_dict[i]
                    or element in column_dict[j]
                    or element in square_dict[(i//3, j//3)]):
                    return False

                row_dict[i].add(element)
                column_dict[j].add(element)
                square_dict[(i//3, j//3)].add(element)

        return True

""" Visualizing the square dictionary
square_dict = {
    (0, 0): {'5', '3', '7'},  # Elements in the top-left 3x3 subgrid
    (0, 1): {'6', '1', '9'},  # Elements in the top-center 3x3 subgrid
    (0, 2): {'8'},            # Elements in the top-right 3x3 subgrid
    (1, 0): {'4'},            # Elements in the middle-left 3x3 subgrid
    (1, 1): {'8', '3'},       # Elements in the middle-center 3x3 subgrid
    (1, 2): set(),            # Empty set for the middle-right 3x3 subgrid
    (2, 0): set(),            # Empty set for the bottom-left 3x3 subgrid
    (2, 1): set(),            # Empty set for the bottom-center 3x3 subgrid
    (2, 2): set()             # Empty set for the bottom-right 3x3 subgrid
}
"""
