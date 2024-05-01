import pygame
from pygame.sprite import Sprite
from settings import Settings
class Bullet(Sprite):
    """ミサイルクラス"""

    def __init__(self, ai_game) -> None:
        """初期化"""
        super().__init__()

        self.screen = ai_game.screen
        self.settings: Settings = ai_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        """ミサイル発射"""

        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """ミサイルを再描画する。"""

        pygame.draw.rect(self.screen, self.color, self.rect)