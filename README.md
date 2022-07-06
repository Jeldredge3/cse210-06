## TEAM to do list:
```
[] Make playerone and playertwo seperate entities.
[] Add a reset button so player's can play another round.
[] Allow both players to collision into eachother.
[] Rename 'snake' folder to 'cycle' without messing up all the existing code.
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
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.```

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
