# APY_Calculator
  For new investors, it can be very confusing to plan how much money they should invest over time, or what they should invest their money into. An interest rate calculator can be a very helpful tool for new investors. It can help them plan future investments and set more realistic goals as they find what they can earn. There are many different aspects to consider in the world of finance, but this calculator makes this aspect a little easier. 
  This program is a basic interest rate calculator made using Python and the Pygame extension. this was made with the intention of creating a simple and user-friendly interface to find out the possible earnings an account of yours may have over time. It currently only calculates each month for a year in the future, but further changes are planned as I continue improving and expanding this application. Hope you find it useful, enjoy!

### <align center> *_How to use:_* ###
  This calculator uses a very simple interface. You are first presented with 5 input boxes: Current Balance, APY Interest, Accrual Frequency(monthly/yearly), Deposit Frequency(weekly/monthly/yearly), and Deposit Amount. After entering info into each box, your results include, Amount earned per month(1-12), Total Deposited, Total Earned, and Final balance after 1 year. You may enter any number, and can even start with a balance of 0 to find how you'd start from scratch.


# More About the Program 

  ## 🔧 _Pygame_ 🔧
  This program requires the usage of a Python extension called  `pygame` in order to create its interactable interface.
  
  1. Pygame is a popular extension module for the Python programming language that allows developers to create interactive games and multimedia applications. It provides powerful tools and libraries for creating and manipulating graphics, sound, and input events.

  2. Pygame is built on top of the SDL (Simple DirectMedia Layer) library, which provides low-level access to computer hardware, such as graphics cards and sound cards. This means that Pygame can create high-performance applications that utilize hardware acceleration for smooth graphics and fast proper processing.

  3. Pygame provides a number of valuable features, such as sprites, collision detection, event handling, and sound effects, which make it easy to create complex games and applications.

  4. It also supports a wide range of file formats for images, sounds, and fonts, making it easy to import and use existing assets in your game or application. Additionally, Pygame provides support for various input devices, such as keyboards, mice, and joysticks, which makes it easy to create interactive applications that respond to user input.

  #### Implementation:
  This extension can be easily implemented like most other functions in Python by beginning the file with:
  
  ```bash
import pygame
```
  #### Example:
   ```bash
  import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
win_width = 640
win_height = 480

# Create the window
win = pygame.display.set_mode((win_width, win_height))

# Set the title of the window
pygame.display.set_caption("My Pygame Window")

# Set the color of the rectangle
rect_color = (255, 0, 0)  # Red

# Set the dimensions and position of the rectangle
rect_x = 100
rect_y = 100
rect_width = 50
rect_height = 50

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    win.fill((255, 255, 255))  # White

    # Draw the rectangle
    pygame.draw.rect(win, rect_color, (rect_x, rect_y, rect_width, rect_height))

    # Update the screen
    pygame.display.update()

# Clean up Pygame
pygame.quit()

```
  This code creates a base display template by setting the height and width of the window, along with functions like `display`, `fill`, and `draw`. 
    - One key function is `display.update()`. This function is necessary in order to constantly update the user's screen when any change is made.
  It also implements a basic running loop that most programs would utilize in order to run the program until an end condition is met.
