# -*- coding: utf-8 -*-
# @Time        : 2019/3/9 15:09
# @Author      : NitroMelon
# @Email       : hwc14@qq.com

from settings import *
from gamedisplay import GameDisplay
from gamestate import GameState
from gameresource import GameResource
import sys
import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(u'俄罗斯方块')
    pygame.key.set_repeat(100, 100)
    game_resource = GameResource()
    game_state = GameState(screen, game_resource)
    game_resource.play_bg_music()

    while True:
        if game_state.piece and game_state.piece.is_at_bottom:
            game_state.touch_bottom()
        if game_state.score >= game_state.difficulty * SCORE_PER_LEVEL:
            game_state.add_difficulty()
        check_events(game_state, game_resource)
        screen.blit(game_resource.load_bg_img(), (0, 0))
        GameDisplay.draw_game_area(game_state, game_resource)
        if game_state.piece:
            GameDisplay.draw_piece(game_state)
        pygame.display.flip()


def check_events(game_state, game_resource):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            on_key_down(event, game_state, game_resource)
        elif event.type == pygame.USEREVENT:
            game_state.piece.move_down()
        elif event.type == pygame.QUIT:
            sys.exit()


def on_key_down(event, game_state, game_resource):
    if event.key == pygame.K_q:
        sys.exit()
    if event.key == pygame.K_m:
        game_resource.pause_bg_music()
    if game_state.stopped:
        if event.key == pygame.K_s:
            game_state.start_game()
    elif game_state.paused:
        if event.key == pygame.K_p:
            game_state.resume_game()
    elif game_state.piece:
        if event.key == pygame.K_LEFT:
            game_state.piece.move_left()
        elif event.key == pygame.K_RIGHT:
            game_state.piece.move_right()
        elif event.key == pygame.K_UP:
            game_state.piece.rotate()
        elif event.key == pygame.K_DOWN:
            game_state.piece.move_down()
        elif event.key == pygame.K_SPACE:
            game_state.piece.go_bottom()
        elif event.key == pygame.K_p:
            game_state.pause_game()
        elif event.key == pygame.K_r:
            game_state.start_game()


if __name__ == '__main__':
    main()
