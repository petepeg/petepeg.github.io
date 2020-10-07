# Peter Pegues - Portfolio

## Boids
This was a quick single day project where I wanted to try and write Boids just based on my interpretation of the rules. I challenged myself not to look at any other implementations of Boids during the process. This turned out to be more difficult than I thought, and has taken much lounger and undergone many revisions to make them flock to my satisfaction.

### Rules
1. **Separation:** steer to avoid crowding local flockmates
2. **Alignment:** steer towards the average heading of local flockmates
3. **Cohesion:** steer to move towards the average position (center of mass) of local flockmates

![Boids](./PyGame-Boids/boids.gif)

## Sudoku
This Sudoku solver uses backtracking to to complete the puzzle. Puzzles are generatorated by filling in random number 1-9 on the diagonal than solving. If the puzzle is solvable than numbers can be removed to create a puzzle of varying difficulty's. The application is reasonably fast solving and generating a puzzle in usually a fraction of a second.

![SudoKu](./PySudoku/Sudoku.png)