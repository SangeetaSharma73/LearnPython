import pygame
import random

# Initialize pygame
pygame.init()

# Set up screen
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🍎 Catch the Falling Fruit!")

# Colors
WHITE = (255, 255, 255)
BROWN = (139, 69, 19)
RED = (255, 0, 0)

# Player (basket)
basket_width = 100
basket_height = 20
basket_x = WIDTH // 2 - basket_width // 2
basket_y = HEIGHT - basket_height - 10
basket_speed = 10

# Fruit
fruit_radius = 15
fruit_x = random.randint(0, WIDTH - fruit_radius)
fruit_y = 0
fruit_speed = 5

# Score
score = 0
font = pygame.font.SysFont(None, 36)

# Clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key press handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x < WIDTH - basket_width:
        basket_x += basket_speed

    # Move fruit
    fruit_y += fruit_speed

    # Check for catch
    if (
        basket_y < fruit_y + fruit_radius < basket_y + basket_height and
        basket_x < fruit_x < basket_x + basket_width
    ):
        score += 1
        fruit_x = random.randint(0, WIDTH - fruit_radius)
        fruit_y = 0

    # If fruit falls off screen
    if fruit_y > HEIGHT:
        fruit_x = random.randint(0, WIDTH - fruit_radius)
        fruit_y = 0

    # Draw basket
    pygame.draw.rect(screen, BROWN, (basket_x, basket_y, basket_width, basket_height))

    # Draw fruit
    pygame.draw.circle(screen, RED, (fruit_x, fruit_y), fruit_radius)

    # Draw score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

# Quit
pygame.quit()
