from settings import *


class Piece(object):
    def __init__(self, shape, screen, game_wall):
        self.x = 4
        self.y = 0
        self.shape = shape        # 值为一个字符。S,  I，J，L，O，T，Z等字母中的一个
        self.rotation = 0
        self.matrix = PIECES[shape][self.rotation].copy()
        self.color = PIECES_COLOR[shape]
        self.screen = screen
        self.game_wall = game_wall
        self.is_at_bottom = False

    def move_left(self):
        if self.can_move_left():
            self.x -= 1

    def move_right(self):
        if self.can_move_right():
            self.x += 1

    def move_down(self):
        if self.can_move_down():
            self.y += 1
        else:
            self.is_at_bottom = True

    def rotate(self):
        if self.can_rotate():
            self.rotation = (self.rotation + 1) % 4
            self.matrix = PIECES[self.shape][self.rotation].copy()
        else:
            return
        if not self.can_move_left():
            while not self.can_move_left():
                self.x += 1
            self.x -= 1
        elif not self.can_move_right():
            while not self.can_move_right():
                self.x -= 1
            self.x += 1
        '''
        if not self.can_move_down():
            while not self.can_move_down():
                self.y -= 1
            self.y += 1
        '''

    def go_bottom(self):
        while self.can_move_down():
            self.y += 1
        self.is_at_bottom = True

    def can_move_down(self):
        for r in range(self.matrix.shape[0]):
            for c in range(self.matrix.shape[1]):
                if self.matrix[r][c]:
                    if self.y + r >= ROW_NUM - 1 or self.game_wall.is_wall(self.y + r + 1, self.x + c):
                        return False
        return True

    def can_move_left(self):
        for r in range(self.matrix.shape[0]):
            for c in range(self.matrix.shape[1]):
                if self.matrix[r][c]:
                    if self.x + c <= 0 or self.game_wall.is_wall(self.y + r, self.x + c - 1):
                        return False
        return True

    def can_move_right(self):
        for r in range(self.matrix.shape[0]):
            for c in range(self.matrix.shape[1]):
                if self.matrix[r][c]:
                    if self.x + c >= COLUMN_NUM - 1 or self.game_wall.is_wall(self.y + r, self.x + c + 1):
                        return False
        return True

    def can_rotate(self):
        after_turn = PIECES[self.shape][(self.rotation + 1) % 4].copy()
        x = self.x
        if x + after_turn.shape[1] > COLUMN_NUM:
            x = COLUMN_NUM - after_turn.shape[1]
        for r in range(after_turn.shape[0]):
            for c in range(after_turn.shape[1]):
                if after_turn[r][c]:
                    if self.game_wall.is_wall(self.y + r, x + c):
                        return False
        return True

    def hit_wall(self):
        for r in range(self.matrix.shape[0]):
            for c in range(self.matrix.shape[1]):
                if self.matrix[r][c]:
                    if self.game_wall.is_wall(self.y + r, self.x + c):
                        return True
        return False
