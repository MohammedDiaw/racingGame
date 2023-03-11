import pygame
import random

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize Pygame
pygame.init()

# Set the width and height of the screen (window)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the window
pygame.display.set_caption("Racing Game")

# Set the clock
clock = pygame.time.Clock()

# Load the car image
car_img = pygame.image.load("car.png")

# Set the initial position of the car
car_x = SCREEN_WIDTH / 2 - 50
car_y = SCREEN_HEIGHT - 150

# Set the initial speed of the car
car_speed_x = 0

# Load the obstacle image
obstacle_img = pygame.image.load("obstacle.png")

# Set the initial position and speed of the obstacle
obstacle_x = random.randint(0, SCREEN_WIDTH - 100)
obstacle_y = -100
obstacle_speed_y = 5

# Set the score
score = 0

# Set the font
font = pygame.font.SysFont(None, 48)

# Set the game loop
game_running = True
while game_running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                car_speed_x = -5
            elif event.key == pygame.K_RIGHT:
                car_speed_x = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                car_speed_x = 0

    # Move the car
    car_x += car_speed_x

    # Wrap the car around the screen
    if car_x < -50:
        car_x = SCREEN_WIDTH - 50
    elif car_x > SCREEN_WIDTH - 50:
        car_x = -50

    # Move the obstacle
    obstacle_y += obstacle_speed_y

    # Spawn a new obstacle when the previous one goes off the screen
    if obstacle_y > SCREEN_HEIGHT:
        obstacle_x = random.randint(0, SCREEN_WIDTH - 100)
        obstacle_y = -100
        score += 1

    # Check for collision
    if car_x + 50 > obstacle_x and car_x < obstacle_x + 100 and car_y + 50 > obstacle_y and car_y < obstacle_y + 100:
        game_running = False

    # Clear the screen
    screen.fill(BLACK)

    # Draw the car and obstacle
    screen.blit(car_img, (car_x, car_y))
    screen.blit(obstacle_img, (obstacle_x, obstacle_y))

    # Draw the score
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
