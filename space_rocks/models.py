from pygame.math import Vector2
# Vector2 offers some functionality, like calculating the distance between vectors and adding or subtracting vectors
from pygame.transform import rotozoom

from utils import load_sprite
from utils import wrap_position, get_random_velocity
from utils import load_sound


class GameObject:
    def __init__(self, position, sprite, velocity):
        """
        position: A point in the center of the object on the 2D screen
        sprite: An image used to display the object
        radius: A value representing the collision zone around the object’s position
        velocity: A value used for movement
        """
        self.position = Vector2(position)
        self.sprite = sprite
        self.radius = sprite.get_width() / 2
        self. velocity = Vector2(velocity)
    
    def draw(self, surface):
        blit_position = self.position - Vector2(self.radius)
        surface.blit(self.sprite, blit_position)
    # game objects have a central position, but blit() requires a top-left corner. 
    # So, the blit position has to be calculated
    # by moving the actual position of the object by a vector:

    def move(self, surface):
        self.position = wrap_position(self.position + self.velocity, surface)
    
    def collides_with(self, other_obj) -> bool:
        distance = self.position.distance_to(other_obj.position)
        return distance < self.radius + other_obj.radius


UP = Vector2(0, -1)


class Spaceship(GameObject):

    MANEUVERABILITY = 3  # The MANEUVERABILITY value determines how fast your spaceship can rotate.
    ACCELERATION = 0.05
    BULLET_SPEED = 3

    def __init__(self, position, create_bullet_callback):
        # Every time the spaceship creates a bullet, it will initialize a Bullet object and then call the callback.
        # The callback will add the bullet to the list of all bullets stored by the game.
        self.create_bullet_callback = create_bullet_callback
        self.laser_sound = load_sound('laser')
        # make a copy of the original UP vector
        self.direction = Vector2(UP)

        super().__init__(position, load_sprite('spaceship'), Vector2(0))

    def rotate(self, clockwise=True):
        sign = 1 if clockwise else -1
        angle = self.MANEUVERABILITY * sign
        self.direction.rotate_ip(angle)

    def draw(self, surface):
        angle = self.direction.angle_to(UP)
        rotated_surface = rotozoom(self.sprite, angle, 1.0)
        rotated_surface_size = Vector2(rotated_surface.get_size())
        blit_position = self.position - rotated_surface_size * 0.5
        surface.blit(rotated_surface, blit_position)

    def accelerate(self):
        self.velocity += self.direction * self.ACCELERATION

    def deaccelerate(self):
        self.velocity -= self.direction * self.ACCELERATION

    def shoot(self):
        bullet_velocity = self.direction * self.BULLET_SPEED + self.velocity
        bullet = Bullet(self.position, bullet_velocity)
        self.create_bullet_callback(bullet)
        self.laser_sound.play()


class Asteroid(GameObject):
    def __init__(self, position, create_asteroid_callback, size=3):
        self.create_asteroid_callback = create_asteroid_callback
        self.size = size

        size_to_scale = {
            3: 1,
            2: 0.5,
            1: 0.25
        }
        # 3 represents big, 2 medium, 1 small asteroid

        scale = size_to_scale[size]
        sprite = rotozoom(load_sprite('asteroid'), 0, scale)

        super().__init__(
            position, sprite, get_random_velocity(1, 3))

    def split(self):
        if self.size > 1:
            for _ in range(2):
                asteroid = Asteroid(
                    self.position, self.create_asteroid_callback, self.size - 1
                )
                self.create_asteroid_callback(asteroid)


class Bullet(GameObject):
    def __init__(self, position, velocity):
        super().__init__(position, load_sprite('bullet'), velocity)

    def move(self, surface):
        self.position = self.position + self.velocity







