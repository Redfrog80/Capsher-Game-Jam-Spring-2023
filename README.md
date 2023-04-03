# Capsher-Game-Jam-Spring-2023  

## Starship Renegade (undecided name)
  
# (Test documentation with some formatting)  fill in the blanks


This is a game built entirely with Python’s PyGame library. The player is a ship trying to survive and defeat the queen of the aliens – but with a twist for the player to discover during gameplay. An executable for Windows has been provided for ease of access.

## Classes
classes and documentation is unfinished
* Base():
* GameObject():
* Camera(): A child of GameObject. This object is used frequently for drawing objects and can be configured to follow an object.
* Playable(): A child of GameObject(). This is the base class for all entities, player or enemy, in the game.
* Enemy(): A child of Playable().
* Assault(): A special type of enemy
* GameWorld(): Container for entities, handles rendering, physics, and garbage collection of destroyed entites. 

## Libraries used
* pygame (main library for coding the game)
* os (for compatibility between files)
* math (for trig calculations and more complicated gameplay features)
* random (for variation in sounds, enemy spawning, etc)

## Roles
* Gage: Concepted enemy classes, created assets, story and text system, sound engine, and start menu
* Hao:  Idk what all everyone did, it's probably best if you put it in yoursleves
* Jeremy: Created the gameWorld class, added collision detection, added garbage collection system.
* Phong:
