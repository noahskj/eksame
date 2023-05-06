import pygame as pg
import random

class Enemy:
    def __init__(self, x, y, img):
        self.img = img
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.rect.width  # define a width attribute
        self.speed = 1

    def move(self):
        dir = random.choice(["left", "right", "up", "down"])
        if dir == "left":
            self.rect.x -= self.speed
        elif dir == "right":
            self.rect.x += self.speed
        elif dir == "up":
            self.rect.y -= self.speed
        elif dir == "down":
            self.rect.y += self.speed

    def draw(self, win):
        win.blit(self.img, self.rect)

    def shoot(self, bullets):
        bullet = Bullet(self.rect.x, self.rect.y)
        bullets.append(bullet)

    def die(self, enemies):
        enemies.remove(self)


class Bullet:
    def __init__(self, x, y):
        self.rect = pg.Rect(x, y, 5, 5)
        self.speed = 5

    def move(self):
        self.rect.y += self.speed

    def draw(self, win):
        pg.draw.rect(win, (255, 0, 0), self.rect)