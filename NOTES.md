Before Tet: 1/26
- Added bullets group
- Completed removing old bullets
- // TODO: why use bullets.copy()

Press ESC key to quit the game

2/22
- Create an alian class
- Build an alien fleet: a group of aliens

2/23
- create fleet filled with rows and columns
- make them move!

3/6
- BUGS with fleet movement -> slide down instead of dropping down (Bao's code works though?) 
-> 3/9: bug fixed (added a break)

3/12
- detect collision with sprite.groupcollide()
- spawn new fleet
- if aliens touch ship -> lose
- reset the game when aliens touch ship
- aliens touch bottom?

3/13
state machine:
    - menu
    - play
    - game over
    - play again
- button for clicking


3/16 TODOs:
- problem with the play button => Deactivate it!
- hiding mouse cursor
- check mouse hover func
- press enter to play -> split code to startgame() func

3/20:
- scoring system
- display score
- algorithm to format number with commas

3/26
- level up: when a fleet is cleared
- dynamic game -> speed up factor + reset speed

3/29
- high score system -> store this number somewhere so that it will not be lost when the game is restarted (JSON)
- had level up mechanism, but no level system yet
-> updated the high score, but score stops rendering (still counting up correctly) -> FIXED

3/30
- How to store high score without losing when we turn off the game?
    -> storing in files: txt file, json: READ + PARSE
    -> database system: MySQL
    -> store in a py file: module: can just import and use directly

4/2
- High score DONE
- Save high score (if current score > high score) back to json when the game restarts


<<<<<<< HEAD
4/12
- Implement the level function
- Draw lives on score board
=======
4/13
- Implement the lives system
- Fix bugs
- Draw hearts
>>>>>>> fa5ffa80
