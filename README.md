Flappy Bird (Python – Pygame Implementation)

This project is a simple implementation of the classic Flappy Bird game using Python and the Pygame library. In this version, the player controls a circular character instead of a bird sprite, keeping the design minimal while focusing on core game mechanics such as movement, collision detection, scoring, and game loop management.

The game features a continuously moving environment where obstacles (pipes) appear at regular intervals with random gaps. The player must navigate the circle through these gaps by controlling its vertical movement. Gravity constantly pulls the circle downward, and the player must press a key (such as the spacebar) to apply an upward force (jump/flap).

The objective of the game is to survive as long as possible while passing through the pipes. Each successful pass increases the score, which is displayed on the screen. The game becomes progressively challenging as the player must time their movements carefully to avoid collisions.

Key components of the game include:
Game Loop: Handles events, updates game state, and renders graphics continuously

Player Movement: Simulates gravity and jump mechanics

Obstacle Generation: Pipes are generated dynamically with random heights

Collision Detection: Detects collisions between the circle and pipes or ground

Score System: Tracks and displays the player’s score

Game Over Logic: Ends the game when a collision occurs and allows restart

This project demonstrates fundamental concepts of game development such as physics simulation, event handling, animation, and real-time rendering using Pygame. It is suitable for beginners who want to understand how 2D games are structured and implemented in Python.
