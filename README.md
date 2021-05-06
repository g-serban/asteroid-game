The project will be broken into ten steps:

    1. Setting up Pygame for a Python project

    2. Handing input in the game

    3. Loading images and showing them on the screen

    4. Creating game objects with an image, a position, and some logic

    5. Moving the spaceship

    6. Moving the asteroids and detecting collisions with the spaceship

    7. Shooting bullets and destroying asteroids

    8. Splitting asteroids into smaller ones

    9. Playing sounds

    10. Handling the end of the game





The game will use the following key mappings:
Right 	Rotate the spaceship right
Left 	Rotate the spaceship left
Up 	Accelerate the spaceship forward
Space 	Shoot
Esc 	Exit the game


There will also be six big asteroids in the game. When a bullet hits a big asteroid, it will split into two medium ones. When a bullet hits a medium asteroid, it will split into two small ones. A small asteroid won’t split but will be destroyed by a bullet.


Game dev terminology:

assets = sounds, fonts, animations, and so on
sprites = images



The game will use vectors to represent positions and directions, as well as some vector operations to move the elements on the screen. Pygame will take care of most of the math

- direction is a vector describing where the spaceship is pointing.
- velocity is a vector describing where the spaceship moves each frame.
- ACCELERATION is a constant number describing how fast the spaceship can speed up each frame.




# In general, the structure of a Pygame program looks like this:


initialize_pygame()

    while True:
# Line 7 starts a loop, called the game loop. Each iteration of this loop generates a single frame of the game and usually performs the following operations:



    handle_input() 
# Input like pressed buttons, mouse motion, and VR controllers position is gathered and then handled.


    process_game_logic() 
# This is where most of the game mechanics are implemented. Here, the rules of physics are applied, collisions are detected and handled, artificial intelligence does its job, and so on.
   

    draw_game_elements()
# If the game hasn’t ended yet, then this is where the frame will be drawn on screen. It will include all the items that are currently in the game and are visible to the player.



