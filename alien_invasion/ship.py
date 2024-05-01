import pygame

class Ship:
    """戦闘機クラス"""

    def __init__(self, ai_game) -> None:
        """初期化"""

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()


        # 戦闘機の画像をローディングし、矩形を取得する。
        self.image = pygame.image.load("alien_invasion/images/ship.bmp")
        self.rect = self.image.get_rect()

        # 戦闘機は常にスクリーンの底部中央で表示される
        self.rect.midbottom = self.screen_rect.midbottom

        # 移動フラグ
        self.moving_right = False
        self.moving_left = False

        self.x = float(self.rect.x)

    def update(self):
        """移動フラグによって、戦闘機の位置を再設定する。"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        """指定の位置で戦闘機を描画する。"""
        self.screen.blit(self.image, self.rect)