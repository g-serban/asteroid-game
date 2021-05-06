import pygame

from utils import load_sprite, get_random_position
from models import Spaceship, Asteroid
from utils import load_sound
from utils import print_text


class SpaceRocks:
    MIN_ASTEROID_DISTANCE = 250

    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((1920, 1080))
        self.background = load_sprite('space', False)
        self.clock = pygame.time.Clock()  # used to limit fps to value of 60 in _draw method
        self.game_over_sound = load_sound('game_over')
        self.victory_sound = load_sound('victory')
        self.asteroid_sound = load_sound('destroyed')
        self.font = pygame.font.Font(None, 64)
        # The constructor of the Font class takes two arguments:
        # The name of the font file, where None means that a default font will be used
        # The size of the font in pixels
        self.message = ''

        self.asteroids = []
        self.bullets = []
        self.spaceship = Spaceship((400, 300), self.bullets.append)

        for _ in range(6):
            while True:
                position = get_random_position(self.screen)
                if (
                        position.distance_to(self.spaceship.position)
                        > self.MIN_ASTEROID_DISTANCE
                ):
                    break

            self.asteroids.append(Asteroid(position, self.asteroids.append))

    def main_loop(self):
        while True:
            self._handle_input()
            self._process_game_logic()
            self._draw()

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("Space Rocks")

    def _handle_input(self):
        # quit options
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN
                and event.key == pygame.K_ESCAPE
            ):
                quit()

            elif (
                self.spaceship
                and event.type == pygame.KEYDOWN
                and event.key == pygame.K_SPACE
            ):
                self.spaceship.shoot()

        # handle input for left arrow or right arrow press
        is_key_pressed = pygame.key.get_pressed()

        if self.spaceship:
            if is_key_pressed[pygame.K_RIGHT]:
                self.spaceship.rotate(clockwise=True)
            elif is_key_pressed[pygame.K_LEFT]:
                self.spaceship.rotate(clockwise=False)
            # handle input for up arrow
            elif is_key_pressed[pygame.K_UP]:
                self.spaceship.accelerate()
            elif is_key_pressed[pygame.K_DOWN]:
                self.spaceship.deaccelerate()

    def _get_game_objects(self):
        game_objects = [*self.asteroids, *self.bullets]

        if self.spaceship:
            game_objects.append(self.spaceship)

        return game_objects

    def _process_game_logic(self):
        for game_object in self._get_game_objects():
            game_object.move(self.screen)

        if self.spaceship:
            for asteroid in self.asteroids:
                if asteroid.collides_with(self.spaceship):
                    self.spaceship = None
                    self.game_over_sound.play()
                    self.message = 'GAME OVER'
                    break

        for bullet in self.bullets[:]:
            for asteroid in self.asteroids[:]:
                if asteroid.collides_with(bullet):
                    self.asteroids.remove(asteroid)
                    self.bullets.remove(bullet)
                    asteroid.split()
                    self.asteroid_sound.play()
                    break

        for bullet in self.bullets[:]:
            #  create a copy of the original list using self.bullets[:].
            #  That’s because removing elements from a list while iterating over it can cause errors.
            if not self.screen.get_rect().collidepoint(bullet.position):
                # Surfaces in Pygame have a get_rect() method that returns a rectangle representing their area.
                # That rectangle, in turn, has a collidepoint() method that returns True if a point
                # is included in the rectangle and False otherwise.
                # Using these two methods, you can check if the bullet has left the screen, and if so,
                # remove it from the list.
                self.bullets.remove(bullet)

        if not self.asteroids and self.spaceship:
            self.message = 'VICTORY'
            self.victory_sound.play()

    def _draw(self):
        self.screen.blit(self.background, (0, 0))

        for game_object in self._get_game_objects():
            game_object.draw(self.screen)

        if self.message:
            print_text(self.screen, self.message, self.font)

        pygame.display.flip()
        self.clock.tick(144)  # limit fps to 144

# TODO  Step 8: Splitting the Asteroids
