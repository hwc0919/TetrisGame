from settings import *
from gamewall import GameWall
from piece import Piece
import random
import time
import pygame


class GameState(object):
    def __init__(self, screen, game_resource):
        self.screen = screen
        self.game_wall = GameWall()
        self.game_resource = game_resource
        self.piece = None
        self.next_piece = Piece(random.choice(PIECE_TYPES), self.screen, self.game_wall)
        self.score = 0
        self.game_round = 0
        self.difficulty = ORIGIN_DIFFICULTY
        self.timer_interval = TIMER_INTERVAL // self.difficulty
        self.game_timer = None
        self.stopped = True
        self.paused = False
        self.rank = []

    def set_timer(self, timer_interval):
        self.game_timer = pygame.time.set_timer(pygame.USEREVENT, timer_interval)

    def add_piece(self):
        self.piece = self.next_piece
        self.next_piece = Piece(random.choice(PIECE_TYPES), self.screen, self.game_wall)

    def add_score(self, score):
        self.score += score

    def add_difficulty(self):
        self.difficulty += 1
        self.set_timer(self.timer_interval // self.difficulty)

    def start_game(self):
        if self.game_round > 0:
            self.game_resource.play_bg_music()
            if self.game_resource.music_muted:
                pygame.mixer.music.pause()

        self.game_resource.gameover_music_played = False
        self.stopped = False
        random.seed(time.time())
        self.set_timer(self.timer_interval)
        self.add_piece()
        self.game_wall.clear()
        if self.score:
            self.rank.append(self.score)
            self.rank.sort()
            self.rank.reverse()
        self.score = 0
        self.paused = False
        self.difficulty = ORIGIN_DIFFICULTY
        self.game_round += 1

    def pause_game(self):
        self.set_timer(0)
        self.paused = True

    def resume_game(self):
        self.set_timer(self.timer_interval)
        self.paused = False

    def touch_bottom(self):
        self.game_wall.add_to_wall(self.piece)
        self.add_score(self.game_wall.eliminate_lines())
        if not self.stopped:
            for c in range(COLUMN_NUM):
                if self.game_wall.is_wall(0, c):
                    self.stopped = True
                    self.game_resource.gameover_music_played = False
                    break
        if not self.stopped:
            self.add_piece()
            if self.piece.hit_wall():
                self.stopped = True
                self.game_resource.gameover_music_played = False
        if self.stopped:
            self.set_timer(0)
            if not self.game_resource.gameover_music_played and not self.game_resource.music_muted:
                self.game_resource.play_gameover_music()
            self.game_resource.gameover_music_played = True
