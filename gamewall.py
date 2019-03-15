from settings import *


class GameWall(object):
    def __init__(self):
        self.game_area = np.zeros((ROW_NUM, COLUMN_NUM), dtype=int)

    def clear(self):
        self.game_area = np.zeros((ROW_NUM, COLUMN_NUM), dtype=int)

    def add_to_wall(self, piece):
        for r in range(piece.matrix.shape[0]):
            for c in range(piece.matrix.shape[1]):
                if piece.matrix[r][c]:
                    self.set_cell(piece.y + r, piece.x + c, piece.shape)

    def set_cell(self, row, col, shape_label):
        self.game_area[row][col] = SHAPE_TO_INT[shape_label]

    def is_wall(self, row, col):
        if row >= ROW_NUM:
            return True
        try:
            if self.game_area[row][col] == 0:
                return False
        except IndexError:
            return False
        return True

    def eliminate_lines(self):
        lines_eliminated = []
        for r in range(ROW_NUM):
            if self.is_full(r):
                lines_eliminated.append(r)
        for r in lines_eliminated:
            self.down(r)
        eliminated_num = len(lines_eliminated)
        assert (0 <= eliminated_num <= 4)
        if eliminated_num < 3:
            score = eliminated_num * 100
        elif eliminated_num == 3:
            score = 400
        else:
            score = 800
        return score

    def is_full(self, r):
        for cell in self.game_area[r]:
            if cell == 0:
                return False
        return True

    def down(self, r):
        self.game_area[1:r + 1] = self.game_area[:r]
        self.game_area[0] = [0] * COLUMN_NUM

    def __str__(self):
        return self.game_area

