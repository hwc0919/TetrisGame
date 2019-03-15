import pygame


class GameResource(object):
    def __init__(self):
        self.img_path = 'image\\'
        self.music_path = 'music\\'
        self.newgame_img = None
        self.pause_img = None
        self.resume_img = None
        self.gameover_img = None
        self.next_piece_img = None
        self.bg_img = None
        self.bg_music = self.music_path + 'bg_music.mp3'
        self.gameover_music = self.music_path + 'gameover_music.mp3'
        self.bg_music_paused = False
        self.gameover_music_played = False
        self.music_muted = False
        pygame.mixer.init()

    def load_newgame_img(self):
        if not self.newgame_img:
            self.newgame_img = pygame.image.load(self.img_path + 'press_s_start.png').convert_alpha()
        return self.newgame_img

    def load_pause_img(self):
        if not self.pause_img:
            self.pause_img = pygame.image.load(self.img_path + 'game_paused.png').convert_alpha()
        return self.pause_img

    def load_resume_img(self):
        if not self.resume_img:
            self.resume_img = pygame.image.load(self.img_path + 'press_p_resume.png').convert_alpha()
        return self.resume_img

    def load_gameover_img(self):
        if not self.gameover_img:
            self.gameover_img = pygame.image.load(self.img_path + 'game_over.png').convert_alpha()
        return self.gameover_img

    def load_next_piece_img(self):
        if not self.next_piece_img:
            self.next_piece_img = pygame.image.load(self.img_path + 'next_piece.png').convert_alpha()
        return self.next_piece_img

    def load_bg_img(self):
        if not self.bg_img:
            self.bg_img = pygame.image.load(self.img_path + 'bg_img.jpg')
        return self.bg_img

    def play_bg_music(self):
        pygame.mixer.music.load(self.bg_music)
        pygame.mixer.music.play(-1)  # -1 指循环播放

    def pause_bg_music(self):
        if not self.music_muted:
            pygame.mixer.music.pause()
            self.music_muted = True
        else:
            pygame.mixer.music.unpause()
            self.music_muted = False

    def play_gameover_music(self):
        pygame.mixer.music.load(self.gameover_music)
        pygame.mixer.music.play(1)


