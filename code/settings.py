from pyray import *
from raylib import *
from random import randint, uniform
from os.path import join

WINDOW_WIDTH, WINDOW_HEIGHT = 1920, 1080
BG_COLOR = (15,10,25,255)
PLAYER_SPEED = 500
LASER_SPEED = 600
METEOR_SPEED_RANGE = [300,400]
METEOR_TIMER_DURATION = 0.4
FONT_SIZE = 120

class Player():
    def __init__(self):
        self.img = load_image(join("..", "images", "spaceship.png"))
        self.pos = Vector2(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        self.direction = Vector2(0, 0)
        self.speed = PLAYER_SPEED
        self.rect = Rectangle(self.pos.x, self.pos.y, self.img.width, self.img.height)
        self.texture = load_texture_from_image(self.img)
        
    def update(self, dt):
        self.direction.x = is_key_down(KEY_RIGHT) - is_key_down(KEY_LEFT)
        self.direction.y = is_key_down(KEY_DOWN) - is_key_down(KEY_UP)
        self.direction = Vector2Normalize(self.direction)

        self.pos.x += self.direction.x * dt * self.speed
        self.pos.y += self.direction.y * dt * self.speed
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y


class Meteor():
    def __init__(self):
        self.img = load_image(join("..", "images", "meteor.png"))
        self.pos = Vector2(randint(0, WINDOW_WIDTH), 0)
        self.direction = Vector2(uniform(-1, 1), 1) #Normalize?
        self.speed = randint(*METEOR_SPEED_RANGE)
        self.rect = Rectangle(self.pos.x, self.pos.y, self.img.width, self.img.height)
        self.texture = load_texture_from_image(self.img)
        
    
    def update(self, dt):
        self.pos.x += self.direction.x * self.speed * dt
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y


class Star():
    def __init__(self):
        self.img = load_image(join("..", "images", "star.png"))
        self.pos = Vector2(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT))
        self.texture = load_texture_from_image(self.img)


class Laser():
    def __init__(self):
        self.img = load_image(join("..", "images", "laser.png"))
        self.pos = Vector2(0, 0)
        self.rect = Rectangle(self.pos.x, self.pos.y, self.img.width, self.img.height)
        self.texture = load_texture_from_image(self.img)
        self.speed = LASER_SPEED
        self.direction = Vector2(0, -1)

    def update(self, pos):
        self.pos.x = pos.x
        self.pos.y = pos.y
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        
        
    def fire(self, dt):
        self.direction = Vector2(0, -1)
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        self.pos.y += self.direction.y * dt * self.speed 

class Explosion():
    def __init__(self):
        self.explosion_frames = [
            load_texture(join("..", "images", "explosion", f"{i}.png")) for i in range(0, 29)     
        ]

    def update(self, pos):
        self.pos.x = pos.x
        self.pos.y = pos.y
        
    