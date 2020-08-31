# portfolio-project

Black Box Game rules: [here](https://en.wikipedia.org/wiki/Black_Box_(game)).  

### Description:
This program represents a popular game called Black Box Game.
The box is  10 x 10 and the boarder is row 0 and 9 and column 0 and 9.
The users enter any number (at least 1) of "atoms" anywhere on the box besides the boarder.
The users can shoot rays only from the boarder but not from the four corners and guess where the atoms are placed based on how the
rays move around the box (hit, reflect, double reflect, and miss).
The score starts at 25 and each entry and exit except previously used entries and exits count as 1 which is subtructed from the score.
Also, every time the user guess where atom is and if it is incorrect, 5 points are subtructed from the score (previously guessed
atoms are not counted).
There are four classes that are Board, Atoms, Rays, and BlackBoxGames to be able to play the game.
Each class has init methods as well as methods to organize and manipulate data as the users play the game.
In BlackBoxGame class, Board, Atoms, and Rays objects are created to keep track of each object's data.
In this version, the guessing player will start with 25 points.  As stated on the Wikipedia page, "Each entry and exit location counts as a point"                   that is deducted from the current score. If any entry/exit location of the current ray is shared with any entry/exit of a previous ray, then it should               not be deducted from the score again. Each incorrect guess of an atom position will cost 5 points, but repeat guesses should not be deducted from the               score again.


Here's a very simple example of how the class could be used:
```
game = BlackBoxGame([(3,2),(1,7),(4,6),(8,8)])
move_result = game.shoot_ray(3,9)
game.shoot_ray(0,2)
guess_result = game.guess_atom(5,5)
score = game.get_score()
atoms = game.atoms_left()
```

