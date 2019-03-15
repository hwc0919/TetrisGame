from settings import *
import pygame


class GameDisplay(object):
    @staticmethod
    def draw_cell(screen, row, col, color):
        cell_pos = (GAME_AREA_LEFT + col * CELL_WIDTH + 1,
                    GAME_AREA_TOP + row * CELL_WIDTH + 1)
        cell_area = (CELL_WIDTH - 1, CELL_WIDTH - 1)
        cell_rect = pygame.Rect(cell_pos, cell_area)
        pygame.draw.rect(screen, color, cell_rect, 0)

    @staticmethod
    def draw_piece(game_state):
        for r in range(game_state.piece.matrix.shape[0]):
            for c in range(game_state.piece.matrix.shape[1]):
                if game_state.piece.matrix[r][c]:
                    GameDisplay.draw_cell(game_state.screen, game_state.piece.y + r, game_state.piece.x + c,\
                                          game_state.piece.color)

    @staticmethod
    def draw_wall(game_state):
        for r in range(ROW_NUM):
            for c in range(COLUMN_NUM):
                if game_state.game_wall.game_area[r][c]:
                    GameDisplay.draw_cell(game_state.screen, r, c,
                                          PIECES_COLOR[INT_TO_SHAPE[game_state.game_wall.game_area[r][c]]])

    @staticmethod
    def draw_score(game_state):
        score_label_font = pygame.font.SysFont('arial', 36)
        score_label_surface = score_label_font.render('Score:', False, SCORE_LABEL_COLOR)
        score_label_position = (GAME_AREA_LEFT + COLUMN_NUM * CELL_WIDTH + 40, GAME_AREA_TOP + 240)
        game_state.screen.blit(score_label_surface, score_label_position)

        score_font = pygame.font.SysFont('arial', 36)
        score_surface = score_font.render(str(game_state.score), False, SCORE_COLOR)
        score_label_width = score_label_surface.get_width()
        score_position = (score_label_position[0] + score_label_width, score_label_position[1])
        game_state.screen.blit(score_surface, score_position)

    @staticmethod
    def draw_game_area(game_state, game_resource):
        border_pos = (GAME_AREA_LEFT, GAME_AREA_TOP)
        border_size = (COLUMN_NUM, ROW_NUM)
        GameDisplay.draw_border(game_state.screen, border_pos, border_size)
        GameDisplay.draw_manual(game_state.screen)
        GameDisplay.draw_wall(game_state)
        GameDisplay.draw_score(game_state)
        GameDisplay.draw_next_piece(game_state, game_resource)
        GameDisplay.draw_rank(game_state)
        GameDisplay.draw_difficulty(game_state)
        if game_state.stopped:
            if game_state.game_round > 0:
                GameDisplay.draw_gameover_prompt(game_state.screen, game_resource)
            GameDisplay.draw_start_prompt(game_state.screen, game_resource)
        if game_state.paused:
            GameDisplay.draw_pause_prompt(game_state.screen, game_resource)

    @staticmethod
    def draw_start_prompt(screen, game_resource):
        start_prompt_position = (GAME_AREA_LEFT + 2 * CELL_WIDTH, GAME_AREA_TOP + 8 * CELL_WIDTH)
        screen.blit(game_resource.load_newgame_img(), start_prompt_position)

    @staticmethod
    def draw_pause_prompt(screen, game_resource):
        pause_prompt_position = (GAME_AREA_LEFT + 2 * CELL_WIDTH, GAME_AREA_TOP + 7 * CELL_WIDTH)
        screen.blit(game_resource.load_pause_img(), pause_prompt_position)

        resume_prompt_position = (GAME_AREA_LEFT + 2 * CELL_WIDTH + 10, GAME_AREA_TOP + 8 * CELL_WIDTH)
        screen.blit(game_resource.load_resume_img(), resume_prompt_position)

    @staticmethod
    def draw_gameover_prompt(screen, game_resource):
        end_prompt_position = (GAME_AREA_LEFT + 2 * CELL_WIDTH, GAME_AREA_TOP + 7 * CELL_WIDTH)
        screen.blit(game_resource.load_gameover_img(), end_prompt_position)

    @staticmethod
    def draw_next_piece(game_state, game_resource):
        border_pos = (GAME_AREA_LEFT + (COLUMN_NUM + 1) * CELL_WIDTH,
                      GAME_AREA_TOP)
        border_size = (4, 4)
        GameDisplay.draw_border(game_state.screen, border_pos, border_size)
        left_top_anchor = NEXT_PIECE_POS[game_state.next_piece.shape]
        for r in range(game_state.next_piece.matrix.shape[0]):
            for c in range(game_state.next_piece.matrix.shape[1]):
                if game_state.next_piece.matrix[r][c]:
                    GameDisplay.draw_cell(game_state.screen, r + left_top_anchor[0], 11 + c + left_top_anchor[1],
                                          game_state.next_piece.color)
        GameDisplay.draw_next_piece_prompt(game_state.screen, game_resource)

    @staticmethod
    def draw_border(screen, border_pos, border_size):
        pos = (border_pos[0] - EDGE_WIDTH,
               border_pos[1] - EDGE_WIDTH)
        size = (border_size[0] * CELL_WIDTH + 2 * EDGE_WIDTH,
                border_size[1] * CELL_WIDTH + 2 * EDGE_WIDTH)
        border_rect = pygame.Rect(pos, size)
        pygame.draw.rect(screen, EDGE_COLOR, border_rect, EDGE_WIDTH)

    @staticmethod
    def draw_next_piece_prompt(screen, game_resource):
        next_piece_prompt_position = (GAME_AREA_LEFT + (COLUMN_NUM + 1.5) * CELL_WIDTH, GAME_AREA_TOP + 4 * CELL_WIDTH)
        screen.blit(game_resource.load_next_piece_img(), next_piece_prompt_position)

    @staticmethod
    def draw_rank(game_state):
        top_list_len = min(len(game_state.rank), 10)
        for i in range(top_list_len):
            GameDisplay.draw_rank_i(game_state, i)

    @staticmethod
    def draw_rank_i(game_state, i):
        score_label_font = pygame.font.SysFont('arial', 36)
        score_label_surface = score_label_font.render('No.' + str(i + 1), False, SCORE_LABEL_COLOR)
        score_label_position = (GAME_AREA_LEFT + (COLUMN_NUM + 1) * CELL_WIDTH, GAME_AREA_TOP + 280 + i * 40)
        game_state.screen.blit(score_label_surface, score_label_position)

        score_font = pygame.font.SysFont('arial', 36)
        score_surface = score_font.render(str(game_state.rank[i]), False, SCORE_COLOR)
        score_label_width = score_label_surface.get_width()
        score_position = (score_label_position[0] + score_label_width + 20, score_label_position[1])
        game_state.screen.blit(score_surface, score_position)

    @staticmethod
    def draw_difficulty(game_state):
        diff_label_font = pygame.font.SysFont('arial', 36)
        diff_label_surface = diff_label_font.render('Difficulty:', False, DIFF_LABEL_COLOR)
        diff_label_position = (GAME_AREA_LEFT + COLUMN_NUM * CELL_WIDTH + 240, GAME_AREA_TOP + 240)
        game_state.screen.blit(diff_label_surface, diff_label_position)

        diff_font = pygame.font.SysFont('arial', 36)
        diff_surface = diff_font.render(str(game_state.difficulty), False, DIFF_COLOR)
        diff_label_width = diff_label_surface.get_width()
        diff_position = (diff_label_position[0] + diff_label_width, diff_label_position[1])
        game_state.screen.blit(diff_surface, diff_position)

    @staticmethod
    def draw_manual(screen):
        base_position_x = 40
        base_position_y = GAME_AREA_TOP + 40
        title_font = pygame.font.SysFont('stkaiti', 28)
        title_surface = title_font.render(u'玩法：', True, TITLE_COLOR)
        title_position = (base_position_x, base_position_y)
        screen.blit(title_surface, title_position)

        base_position_y += 60
        gamectrl_label_font = pygame.font.SysFont('stkaiti', 24)
        gamectrl_label_surface = gamectrl_label_font.render(u'游戏控制', True, TITLE_COLOR)
        gamectrl_label_position = (base_position_x, base_position_y)
        screen.blit(gamectrl_label_surface, gamectrl_label_position)

        base_position_y += 40
        man_font = pygame.font.SysFont('stkaiti', 20)
        man_down_surface = man_font.render(u'开始：s字母键；退出：q字母键', False, CNCHAR_COLOR)
        man_down_position = (base_position_x, base_position_y)
        screen.blit(man_down_surface, man_down_position)

        base_position_y += 40
        man_font = pygame.font.SysFont('stkaiti', 20)
        man_pause_surface = man_font.render(u'暂停/继续：p字母键', False, CNCHAR_COLOR)
        man_pause_position = (base_position_x, base_position_y)
        screen.blit(man_pause_surface, man_pause_position)

        base_position_y += 40
        man_font = pygame.font.SysFont('stkaiti', 20)
        man_restart_surface = man_font.render(u'重玩：r字母键', False, CNCHAR_COLOR)
        man_restart_position = (base_position_x, base_position_y)
        screen.blit(man_restart_surface, man_restart_position)

        base_position_y += 40
        man_font = pygame.font.SysFont('stkaiti', 20)
        man_music_surface = man_font.render(u'暂停/继续播放音乐：m字母键', False, CNCHAR_COLOR)
        man_music_position = (base_position_x, base_position_y)
        screen.blit(man_music_surface, man_music_position)

        base_position_y += 60
        gamectrl_label_font = pygame.font.SysFont('stkaiti', 24)
        gamectrl_label_surface = gamectrl_label_font.render(u'方块控制', True, TITLE_COLOR)
        gamectrl_label_position = (base_position_x, base_position_y)
        screen.blit(gamectrl_label_surface, gamectrl_label_position)

        base_position_y += 40
        man_font = pygame.font.SysFont('stkaiti', 20)
        man_down_surface = man_font.render(u'翻转：上方向键；下移：下方向键', False, CNCHAR_COLOR)
        man_down_position = (base_position_x, base_position_y)
        screen.blit(man_down_surface, man_down_position)

        base_position_y += 40
        man_move_surface = man_font.render(u'左移：左方向键；右移：右方向键', False, CNCHAR_COLOR)
        man_move_position = (base_position_x, base_position_y)
        screen.blit(man_move_surface, man_move_position)

        base_position_y += 40
        man_speed_surface = man_font.render(u'快速到底：空格 键', False, CNCHAR_COLOR)
        man_speed_position = (base_position_x, base_position_y)
        screen.blit(man_speed_surface, man_speed_position)
