# Capsher-Game-Jam-Spring-2023  

## Starship Renegade [Team: S.C.R.A.P.]

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
* Gage: Concepted enemy classes, created assets, story and text system, sound engine, and start menu.
* Hao: 
* Jeremy: Created the gameWorld class, added collision detection, added garbage collection system, added particle system.
* Phong:

## What we weren't able to finish
* Sound system. We resorted to removing implemenation of sounds and directly pasting music to the PyGame mixer.
* Text and plot system (in Gage branch.) We had a plot for the game to create fading text in the background giving hints and a monologue.
* Polishing. The event system needs work and we currently don't have a respawn mechanic.
