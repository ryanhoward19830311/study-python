import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """ゲームのリソース管理"""

    def __init__(self) -> None:
        """初期化"""

        pygame.init()
        self.settings = Settings()

        # self.screen = pygame.display.set_mode((
        #     self.settings.screen_width, self.settings.screen_height
        # ))

        # フルスクリーンモード
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """ゲームを始まる"""

        while True:

            self._check_events()
            self.ship.update()
            self._update_bullet()
            self._update_screen()



    def _check_events(self):
        """キーとマウスイベントをリスニング"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event=event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event=event)

    def _check_keydown_events(self, event):
        """キーダウンイベント処理"""
        if event.key == pygame.K_RIGHT:
            # 右へ移動開始
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # 左へ移動開始
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """キーアップイベント処理"""
        if event.key == pygame.K_RIGHT:
            # 右へ移動終了
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            # 左へ移動終了
            self.ship.moving_left = False

    def _fire_bullet(self):
        """ミサイル発射"""

        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet:Bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullet(self):
        """ミサイル発射再描画"""
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
#        print(len(self.bullets))

    def _update_screen(self):
        """画面再描画"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()