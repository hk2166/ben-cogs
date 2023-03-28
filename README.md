***Flight***
The Flight cog provides a game that simulates flying through different levels with different obstacles. The user must choose an aircraft and then navigate through each level, avoiding the obstacles, in order to complete the game.

*Commands*
[p]start
Begins the game. This command resets the game state, allowing the user to choose a new aircraft and start at level 1.

[p]aircraft
Allows the user to choose their aircraft. This command presents the user with a list of aircraft to choose from, and then sets the chosen aircraft as the user's aircraft for the rest of the game.

[p]help
Shows a list of available commands for the Flight cog.

[p]left
Move the aircraft to the left.

[p]right
Move the aircraft to the right.

[p]up
Move the aircraft up.

[p]down
Move the aircraft down.

Game State
The Flight cog maintains several pieces of game state, including the user's chosen aircraft, the current level, the user's score, and the obstacles for each level.

The obstacles for each level are stored as a list of lists, where each sub-list contains the obstacles for that level. The obstacles are randomly generated for each level using the list of obstacles for that level.





WeirdImages:

A Red Discord bot cog for generating and manipulating weird images.

***Requirements:***

Python 3.6+
discord.py
redbot.core
Pillow

***Installation:***

To install the WeirdImages cog, use the following command in your Red Discord bot instance:


[p]cog install weirdimages
Commands
weird
Generates a weird image with random shapes and colors, applies filters, and sends it to the chat.

Usage: [p]weird [size]

***Arguments:***

size: the size of the image (default: 500)
Cooldown: 15 seconds

***imagemanipulation:***
 This cog provides the following commands:
 
  [p]blur: Applies a Gaussian blur to an attached image.
  
  [p]circle: Draws a circle on an attached image.
  
  [p]grayscale: Converts an attached image to grayscale.
  
  [p]flip: Flips an attached image horizontally.
  




cursed
Combines two images in a cursed way and sends the result to the chat.

Usage: [p]cursed [image1] [image2]

Arguments:

image1: the URL or attachment of the first image
image2: the URL or attachment of the second image
Cooldown: 15 seconds




#still a wip
Filters
The following filters can be applied to images generated by the weird command:

CONTOUR: Finds the edges in an image and enhances them
BLUR: Blurs the image
DETAIL: Enhances the details in an image
EDGE_ENHANCE: Enhances the edges in an image
EDGE_ENHANCE_MORE: Enhances the edges in an image more than EDGE_ENHANCE
EMBOSS: Applies an emboss effect to an image
FIND_EDGES: Finds the edges in an image
SHARPEN: Sharpens an image
SMOOTH: Smooths an image
SMOOTH_MORE: Smooths an image more than SMOOTH
Example
To generate a weird image with size 800, use the following command:


[p]weird 800
To combine two images in a cursed way, use the following command:

[p]cursed https://example.com/image1.png https://example.com/image2.png
I hope this helps! Let me know if you have any questions or need further assistance.
