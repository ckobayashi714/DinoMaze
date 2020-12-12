# Design of Game

## Story

The story takes place during the era of dinosaurs. The player is a green dinosaur who has set out on a quest to save the planet from being destroyed. You are tasked to collect more mushrooms than your opponent; once you've done that, exit the maze before the timer runs out or before the opponent catches up to you.

## The problem at hand

You must not let the clock run out, and you must collect more than your opponent to exit the maze freely; otherwise, you lose. You must not let your opponent catch up to you before you exit the maze.

## What will be incorporated

We will use sprites with images of dinosaurs and background images that match the period. We will incorporate images, music, and sound effects and use a timer and score card to keep track of the player's progress and how many mushrooms each has collected.

![Design Rules](/design/rules.png)

![Enemy Design and Rules](/design/enemy.png)

![Timer Design](/design/timer.png)

## Dino Maze 

+ Audience: Novice players with some knowledge of computers.
+ System requirements: Any OS as long as Python compiler is installed
+ Gameplay images:

![Menu Design](/design/menu.png)

![Backstory](/design/backstory.png)

## Artificial Intelligence added to Game

+ So the green dino could play against an opponent, we incorporated Artificial Intelligence into this game by implementing the blue dino with a BFS Breadth-First Search function called findPlayer and findMushroom. We added 3 levels of difficulty: Easy, Medium, and Hard. This will change how fast the AI takes his next step.
+ We created the illusion of multiple levels by randomizing each maze's creation at the start of each game. We implemented this using the DFS Depth-First Search function called createMaze and finalizeMaze
