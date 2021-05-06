import random

from pygame.image import load
from pygame.math import Vector2
from pygame.mixer import Sound
from pygame import Color


def load_sprite(name, with_alpha=True):
    path = f'assets\\sprites\\{name}.png'
    loaded_sprite = load(path)

    if with_alpha:
        return loaded_sprite.convert_alpha()
    else:
        return loaded_sprite.convert()


def wrap_position(position, surface):
    x, y = position
    w, h = surface.get_size()
    # By using the modulo operator on the following line, we make sure that the position (of the spaceship or asteroids)
    # never leaves the area of the given surface.
    return Vector2(x % w, y % h)


def get_random_position(surface):
    return Vector2(
        random.randrange(surface.get_width()),
        random.randrange(surface.get_height())
    )


def get_random_velocity(min_speed, max_speed):
    speed = random.randint(min_speed, max_speed)
    angle = random.randrange(0, 360)
    return Vector2(speed, 0).rotate(angle)


def load_sound(name):
    path = f'assets\\sounds\\{name}.wav'
    return Sound(path)


def print_text(surface, text, font, color=Color('orangered')):
    text_surface = font.render(text, True, color)

    rect = text_surface.get_rect()
    rect.center = Vector2(surface.get_size()) / 2

    surface.blit(text_surface, rect)






