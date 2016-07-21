"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)
colors = [BLACK, GREEN, BLUE, RED, GREY, WHITE]






def random_color():
    return random.choice(colors)

# initialize the pygame class
pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Set the title of the window
pygame.display.set_caption("CityScroller")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

speed = 4



class Building():
    def __init__(self, x_point, y_point, width, height, color):
        self.x_point = x_point
        self.y_point = y_point
        self.width = width
        self.height = height
        self.color = color


    """
    This class will be used to create the building objects.

    It takes:
      x_point - an integer that represents where along the x-axis the building will be drawn
      y_point - an integer that represents where along the y-axis the building will be drawn
      Together the x_point and y_point represent the top, left corner of the building

      width - an integer that represents how wide the building will be in pixels.
            A positive integer draws the building right to left(->).
            A negative integer draws the building left to right (<-).
      height - an integer that represents how tall the building will be in pixels
            A positive integer draws the building up 
            A negative integer draws the building down 
      color - a tuple of three elements which represents the color of the building
            Each element being a number from 0 - 255 that represents how much red, green and blue the color should have.

    It depends on:
        pygame being initialized in the environment.
        It depends on a "screen" global variable that represents the surface where the buildings will be drawn

    """

    def draw(self, x_point):
        pygame.draw.rect(screen, self.color, (self.x_point, self.y_point, self.width, self.height))

        """
        uses pygame and the global screen variable to draw the building on the screen
        """

    def move(self, speed):
        self.x_point += speed

        """
        Takes in an integer that represents the speed at which the building is moving
            A positive integer moves the building to the right ->
            A negative integer moves the building to the left  <-
        Moves the building horizontally across the screen by changing the position of the
        x_point by the speed
        """


class cloud():
    def __init__(self, screen, x_position, y_position):
        self.screen = screen
        self.x_position = x_position
        self.y_position = y_position


    def create_cloud(self):
        cloud = pygame.image.load("clouds.png")
        cloud = pygame.transform.scale(cloud, (80,35))
        self.x_position = random.randint(0,800)
        self.y_position = random.randint(0, 100)
        screen.blit(cloud, (self.x_position, self.y_position))

    def move_cloud(self,speed):
        self.x_position += speed

# building1 = Building(800+building_width, 500-building_height, building_width, building_height, colors[colors_index])


class Scroller(object):
    """
    Scroller object will create the group of buildings to fill the screen and scroll

    It takes:
        width - an integer that represents in pixels the width of the scroller
            This should only be a positive integer because a negative integer will draw buildings outside of the screen
        height - an integer that represents in pixels the height scroller
            A negative integer here will draw the buildings upside down.
        base - an integer that represents where along the y-axis to start drawing buildings for this
            A negative integer will draw the buildings off the screen
            A smaller number means the buildings will be drawn higher up on the screen
            A larger number means the buildings will be drawn further down the screen
            To start drawing the buildings on the bottom of the screen this should be the height of the screen
        color - a tuple of three elements which represents the color of the building
              Each element being a number from 0 - 255 that represents how much red, green and blue the color should have.
        speed - An integer that represents how fast the buildings will scroll

    It depends on:
        A Building class being available to create the building objects.
        The building objects should have "draw" and "move" methods.

    Other info:
        It has an instance variable "buildings" which is a list of buildings for the scroller
    """

    def __init__(self, width, height, base, color, speed):
        self.width = width
        self.height = height
        self.base = base
        self.color = color
        self.speed = speed
        self.building_list = []        
        self.combined_width = 0
        self.create_buildings()
        

    def create_buildings(self):
        # for building in self.building_list:
        #     self.combined_width += building.width
        while self.combined_width <= self.width:
            self.create_building(self.combined_width)
        """
        Will call create_building until there the buildings fill up the width of the
        scroller.
        """

    def create_building(self, x_location):
        building_width = random.randint(10,40)
        building_height = random.randint(-300,0)
        self.combined_width += building_width
        building1 = Building(x_location, 600, building_width, building_height, self.color)
        self.building_list.insert(0, building1)

        """
        takes in an x_location, an integer, that represents where along the x-axis to
        put a building.
        Adds a building to list of buildings.
        """

    def draw_buildings(self):
        for current_building in self.building_list:
            current_building.draw(self.combined_width)
        """
        This calls the draw method on each building.
        """

    def move_buildings(self):
        for current_building in self.building_list:
            current_building.move(self.speed)

        if self.building_list[-1].x_point > SCREEN_WIDTH:
            self.building_list.remove(self.building_list[-1])
        if self.building_list[0].x_point > 0:
            width = random.randint(10,90)
            x_location = self.building_list[0].x_point - width 
            building1 = Building(x_location, 600, width, random.randint(-300,0), self.color)
            self.building_list.insert(0, building1)

        # if self.building_list[0].x_point < -100:
        #     self.building_list.remove(self.building_list[0])
        # if self.building_list[-1].x_point < SCREEN_WIDTH:
        #     width = random.randint(60,100)
        #     x_location = self.building_list[-1].x_point + width - 10
        #     building1 = Building(x_location, 600, width, random.randint(-300,-100), self.color)
        #     self.building_list.insert(800, building1)

            
        """
        This calls the move method on each building passing in the speed variable
        As the buildings move off the screen a new one is added.
        """

# class cloud_scroller(): 
#     def __init__(self, cloud_speed):
#         self.cloud_speed = speed
#         self.cloud_list = []
#         self.create_clouds()

#     def create_clouds(self):
#         for i in range(10):
#             self.create_cloud()
    
#     def create_cloud(self):
#         cloud_height = random.randint(0,13)
#         cloud_width = random.randint(0,150)
#         cloud1 = cloud(screen, cloud_height, cloud_width)
#         self.cloud_list.append(cloud1)
#         print(len(self.cloud_list))

#     def draw_cloud(self):
#         for current_cloud in self.cloud_list:
#             current_cloud.create_cloud()
        
#     def move_cloud(self):
#         for current_cloud in self.cloud_list:
#             current_cloud.move_cloud(self.cloud_speed)


# FRONT_SCROLLER_COLOR = (0,0,30)
# MIDDLE_SCROLLER_COLOR = (30,30,100)
# BACK_SCROLLER_COLOR = (50,50,150)
# BACKGROUND_COLOR = (17, 9, 89)

# front_scroller = Scroller(SCREEN_WIDTH, 500, SCREEN_HEIGHT, FRONT_SCROLLER_COLOR, 3)
# middle_scroller = Scroller(SCREEN_WIDTH, 200, (SCREEN_HEIGHT - 50), MIDDLE_SCROLLER_COLOR, 2)
# back_scroller = Scroller(SCREEN_WIDTH, 20, (SCREEN_HEIGHT - 100), BACK_SCROLLER_COLOR, 1)
# cloud1 = cloud_scroller(1)
# # -------- Main Program Loop -----------
# while not done:
     

#     # --- Main event loop
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True

#     # --- Game logic should go here

#     # --- Screen-clearing code goes here

#     # Here, we clear the screen to white. Don't put other drawing commands
#     # above this, or they will be erased with this command.

#     # If you want a background image, replace this clear with blit'ing the
#     # background image.
#     screen.fill(BACKGROUND_COLOR)

#     # --- Drawing code should go here

#     back_scroller.draw_buildings()
#     back_scroller.move_buildings()
#     middle_scroller.draw_buildings()
#     middle_scroller.move_buildings()
#     front_scroller.draw_buildings()
#     front_scroller.move_buildings()
#     # cloud1.draw_cloud()
#     # cloud1.move_cloud()




#     # --- Go ahead and update the screen with what we've drawn.
#     pygame.display.flip()

#     # --- Limit to 60 frames per second
#     clock.tick(60)

# # Close the window and quit.
# pygame.quit()
# exit() # Needed when using IDLE
