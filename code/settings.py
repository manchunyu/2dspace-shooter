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

class Sprite:
    def __init__(self, img, pos):
        self.img = img
        self.pos = pos
    
        
class Player(Sprite):
    def __init__(self):
        super().__init__(
            load_image(join("..", "images", "spaceship.png")), 
            Vector2(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2),
        )
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


class Meteor(Sprite):
    def __init__(self):
        super().__init__(
            load_image(join("..", "images", "meteor.png")), 
            Vector2(randint(0, WINDOW_WIDTH), 0),
        )
        self.direction = Vector2(uniform(-1, 1), 1) #Normalize?
        self.speed = randint(*METEOR_SPEED_RANGE)
        self.rect = Rectangle(self.pos.x, self.pos.y, self.img.width, self.img.height)
        self.texture = load_texture_from_image(self.img)
    
    def update(self, dt):
        self.pos.x += self.direction.x * self.speed * dt
        self.pos.y += self.direction.y * self.speed * dt
    

class Star(Sprite):
    def __init__(self):
        super().__init__(
            load_image(join("..", "images", "star.png")),
            Vector2(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)),
        )
        self.texture = load_texture_from_image(self.img)

