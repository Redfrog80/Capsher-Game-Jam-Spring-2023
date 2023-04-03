# Capsher-Game-Jam-Spring-2023  

## R.A.G.E. Shooter [Team: S.C.R.A.P.] (Spaghetti Code Running Advanced Programs)

This is a game built entirely with Python’s PyGame library. The player is a ship trying to survive and defeat the queen of the aliens – but with a twist for the player to discover during gameplay. An executable for Windows has been provided for ease of access.  

See how long you can survive! 

## How to play:
* W and S to accelerate/decelerate
* A and D to turn
* Mouse to aim and LMB to shoot

## Classes
* Base(): Template of all objects.
* GameObject(): The basic game object: Children can be destroyed, supported, and rendered.
* Camera(): A child of Base(). This object is used frequently for drawing objects and can be configured to follow an object. Only renders objects inside of a set bound.
* Playable(): A child of GameObject(). This is the base class for all entities, player or enemy, in the game.
* Enemy(): A child of Playable(). Basic enemy type, determines tracking, movement, and behavior. Contains 4 enemy types.
* GameWorld(): Container for entities, handles rendering, physics, and garbage collection of destroyed entites.
* Sound_class: An unfinished class that contains sound randomization and simplified playing.

## Libraries used
* PyGame (main library for coding the game)
* Internal libraries: math, random

## Roles
* Gage: Concepted enemy classes, created sounds/music, created sprites, story and text system, sound engine, and start menu.
* Hao: 
* Jeremy: Created the gameWorld class, added collision detection, added garbage collection system, added particle system.
* Phong:

## What we weren't able to finish
* Sound system. We resorted to removing implemenation of sounds and directly pasting music to the PyGame mixer. Successfully implemented music, but didn't push in time.
* UI
* Text and plot system (in Gage's branch.) We had a plot for the game to create fading text in the background giving hints and a monologue.
* Polishing. The event system needs work and we currently don't have a respawn mechanic. Also, enemies spawn way too much. Don't tell anyone, this was intentional. Also, we used the wrong player sprite.

## Assets
* Sounds/music created in Ableton
* Sprites created in Blender 3.5
