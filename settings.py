import numpy as np


SCREEN_WIDTH = 1200    # 窗口宽度
SCREEN_HEIGHT = 900    # 窗口高度
CELL_WIDTH = 40         # 方块在20x10个单元格组成的游戏区内移动。每个单元格的边长是40个像素。
EDGE_WIDTH = 5
COLUMN_NUM = 10
ROW_NUM = 20
GAME_AREA_WIDTH = CELL_WIDTH * COLUMN_NUM       # 一行10个单元格
GAME_AREA_HEIGHT = CELL_WIDTH * ROW_NUM         # 一共20行
GAME_AREA_LEFT = (SCREEN_WIDTH - GAME_AREA_WIDTH) // 2      # 游戏区左侧的空白区的宽度
GAME_AREA_TOP = SCREEN_HEIGHT - GAME_AREA_HEIGHT - 50         # 游戏区顶部的空白区的宽度
EDGE_COLOR = (0, 0, 0)          # 游戏区单元格边界线的颜色。
CELL_COLOR = (100, 100, 100)    # 单元格填充色。
BG_COLOR = (230, 230, 230)      # 窗口背景色
SCORE_LABEL_COLOR = (0, 0, 0)
SCORE_COLOR = (255, 0, 0)
DIFF_LABEL_COLOR = (0, 0, 0)
DIFF_COLOR = (255, 0, 0)
TITLE_COLOR = (255, 255, 255)
CNCHAR_COLOR = (255, 255, 255)

TIMER_INTERVAL = 1000
SCORE_PER_LEVEL = 2000

ORIGIN_DIFFICULTY = 1

I_SHAPE_TEMPLATE = [np.array([(0, 1),
                              (0, 1),
                              (0, 1),
                              (0, 1)]),
                    np.array([(0, 0, 0, 0),
                              (1, 1, 1, 1)]),
                    np.array([(0, 1),
                              (0, 1),
                              (0, 1),
                              (0, 1)]),
                    np.array([(0, 0, 0, 0),
                              (1, 1, 1, 1)])]

J_SHAPE_TEMPLATE = [np.array([(1, 0, 0),
                              (1, 1, 1)]),
                    np.array([(1, 1),
                              (1, 0),
                              (1, 0)]),
                    np.array([(1, 1, 1),
                              (0, 0, 1)]),
                    np.array([(0, 1),
                              (0, 1),
                              (1, 1)])]

L_SHAPE_TEMPLATE = [np.array([(0, 0, 1),
                              (1, 1, 1)]),
                    np.array([(1, 0),
                              (1, 0),
                              (1, 1)]),
                    np.array([(1, 1, 1),
                              (1, 0, 0)]),
                    np.array([(1, 1),
                              (0, 1),
                              (0, 1)])]

O_SHAPE_TEMPLATE = [np.array([(1, 1),
                              (1, 1)]),
                    np.array([(1, 1),
                              (1, 1)]),
                    np.array([(1, 1),
                              (1, 1)]),
                    np.array([(1, 1),
                              (1, 1)])]

S_SHAPE_TEMPLATE = [np.array([(0, 1, 1),
                              (1, 1, 0)]),
                    np.array([(1, 0),
                              (1, 1),
                              (0, 1)]),
                    np.array([(0, 1, 1),
                              (1, 1, 0)]),
                    np.array([(1, 0),
                              (1, 1),
                              (0, 1)])]

T_SHAPE_TEMPLATE = [np.array([(0, 1, 0),
                              (1, 1, 1)]),
                    np.array([(1, 0),
                              (1, 1),
                              (1, 0)]),
                    np.array([(1, 1, 1),
                              (0, 1, 0)]),
                    np.array([(0, 1),
                              (1, 1),
                              (0, 1)])]

Z_SHAPE_TEMPLATE = [np.array([(1, 1, 0),
                              (0, 1, 1)]),
                    np.array([(0, 1),
                              (1, 1),
                              (1, 0)]),
                    np.array([(1, 1, 0),
                              (0, 1, 1)]),
                    np.array([(0, 1),
                              (1, 1),
                              (1, 0)])]

PIECE_TYPES = ['I', 'J', 'L', 'O', 'S', 'T', 'Z']

PIECES = {'I': I_SHAPE_TEMPLATE,
          'J': J_SHAPE_TEMPLATE,
          'L': L_SHAPE_TEMPLATE,
          'O': O_SHAPE_TEMPLATE,
          'S': S_SHAPE_TEMPLATE,
          'T': T_SHAPE_TEMPLATE,
          'Z': Z_SHAPE_TEMPLATE}

I_COLOR = (135, 206, 235)
J_COLOR = (0, 0, 139)
L_COLOR = (218, 165, 32)
O_COLOR = (255, 215, 0)
S_COLOR = (0, 255, 0)
T_COLOR = (128, 0, 128)
Z_COLOR = (255, 0, 0)

PIECES_COLOR = {'I': I_COLOR,
                'J': J_COLOR,
                'L': L_COLOR,
                'O': O_COLOR,
                'S': S_COLOR,
                'T': T_COLOR,
                'Z': Z_COLOR}

INT_TO_SHAPE = {1: 'I', 2: 'J', 3: 'L', 4: 'O', 5: 'S', 6: 'T', 7: 'Z'}
SHAPE_TO_INT = {'I': 1, 'J': 2, 'L': 3, 'O': 4, 'S': 5, 'T': 6, 'Z': 7}


NEXT_PIECE_POS = {'I': (0, 0.5),
                  'J': (1, 0.5),
                  'L': (1, 0.5),
                  'O': (1, 1),
                  'S': (1, 0.5),
                  'T': (1, 0.5),
                  'Z': (1, 0.5)}
