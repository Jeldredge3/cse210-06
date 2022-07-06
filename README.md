## TEAM to do list:
```
Priorities:
[ ] Create enemies that start at the top and move down towards the player.
[ ] Make enemies able to collide with bullets.
[ ] Allow the player's segments to be able to collide with enemies
[ ] Create pickup items that can be collected by the player to grant Health, Lives, or Score.
[ ] Create a child class of pickup objects that upgrades the player's weapon.
Optional:
[ ] Add sound files to the game along with background music
[ ] Create more powerups
[ ] Add hitpoints to enemies to make them more resistant to bullets.
[ ] Make a class of enemy that can shoot bullets at the player
[ ] Create a time delay when the player loses a life
[ ] Make the 'P' key pause the game and all entities on the screen. 
[ ] Mess around with the code!
[ ] Clean up & simplify any messy parts of the code.
Completed:
[v] Setup the layout of the game and allow for easy additions to be made.
[v] Create ship that moves up, down, left, right using 'W'A'S'D'
[v] Make the ship shoot when pressing 'space'
[v] Track the player's lives, health, and score
[v] End the game when player's lives and health hit 0.
```
---

# cse210-06
Assignment for Week 11 - Team Code Submission


# Starship
Starship is a fixed shooter game where the player controls a plane and shoots projectiles to destroy oncoming planes & objects.

## Getting Started
---
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.

```
python3 starship 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- starship            (source code for game)
  +-- game              (specific game classes)
    +-- casting         (classes for the display, enemies, pickups, and player)
    +-- directing       (controls the sequence of play)
    +-- scripting       (classes for controlling, drawing, handling collisions, updates, and auto-moving)
    +-- services        (classes for the keyboard & video services)
  +-- __main__.py       (entry point for program)
  +-- constants.py      (universal unchanging variables)
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

## Authors
--- Herrera Axel
--- Jordan Eldredge
--- Jonathan Troche
--- Igor
