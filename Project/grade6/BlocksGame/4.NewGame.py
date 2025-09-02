import pygame
import random
import os

# Game settings
ROWS, COLS = 10, 10
BLOCK_SIZE = 40
WIDTH, HEIGHT = COLS * BLOCK_SIZE, ROWS * BLOCK_SIZE
TOP_MARGIN = 40

COLORS = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255),
    (255, 255, 0), (255, 0, 255), (0, 255, 255)
]

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT + TOP_MARGIN))
pygame.display.set_caption("Falling Block Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

high_score_file = "highscore.txt"
def load_high_score():
    if os.path.exists(high_score_file):
        with open(high_score_file, 'r') as f:
            return int(f.read())
    return 0

def save_high_score(score):
    with open(high_score_file, 'w') as f:
        f.write(str(score))

def create_grid(locked={}):
    grid = [[(0, 0, 0) for _ in range(COLS)] for _ in range(ROWS)]
    for (x, y), color in locked.items():
        if y >= 0:
            grid[y][x] = color
    return grid

def draw_grid(surface, grid, current_shape, current_color, current_pos, score, high_score):
    surface.fill((30, 30, 30))
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    high_score_text = font.render(f"High Score: {high_score}", True, (255, 255, 255))
    surface.blit(score_text, (WIDTH -370, 5))
    surface.blit(high_score_text, (WIDTH - 200, 5))

    for y in range(ROWS):
        for x in range(COLS):
            pygame.draw.rect(surface, grid[y][x], (x * BLOCK_SIZE, y * BLOCK_SIZE + TOP_MARGIN, BLOCK_SIZE, BLOCK_SIZE))

    for dx, dy in current_shape:
        x = current_pos[0] + dx
        y = current_pos[1] + dy
        if 0 <= x < COLS and 0 <= y < ROWS:
            pygame.draw.rect(surface, current_color, (x * BLOCK_SIZE, y * BLOCK_SIZE + TOP_MARGIN, BLOCK_SIZE, BLOCK_SIZE))

    for x in range(COLS):
        pygame.draw.line(surface, (50, 50, 50), (x * BLOCK_SIZE, TOP_MARGIN), (x * BLOCK_SIZE, HEIGHT + TOP_MARGIN))
    for y in range(ROWS):
        pygame.draw.line(surface, (50, 50, 50), (0, y * BLOCK_SIZE + TOP_MARGIN), (WIDTH, y * BLOCK_SIZE + TOP_MARGIN))

    pygame.display.update()

def generate_shape():
    num_blocks = random.randint(1, 4)
    color = random.choice(COLORS)
    shape = [(0, 0)]
    visited = set(shape)
    while len(shape) < num_blocks:
        bx, by = random.choice(shape)
        direction = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        new_block = (bx + direction[0], by + direction[1])
        if new_block not in visited and -2 <= new_block[0] <= 2 and -2 <= new_block[1] <= 2:
            visited.add(new_block)
            shape.append(new_block)
    return shape, color

def is_valid(pos, shape, grid):
    for dx, dy in shape:
        x = pos[0] + dx
        y = pos[1] + dy
        if x < 0 or x >= COLS or y >= ROWS:
            return False
        if y >= 0 and grid[y][x] != (0, 0, 0):
            return False
    return True

def get_block_positions(pos, shape):
    return [(pos[0] + dx, pos[1] + dy) for dx, dy in shape]

def lock_shape(pos, shape, color, locked):
    for x, y in get_block_positions(pos, shape):
        if y >= 0:
            locked[(x, y)] = color

def clear_rows(grid, locked):
    full_rows = []
    for y in range(ROWS):
        if (0, 0, 0) not in grid[y]:
            full_rows.append(y)
    if not full_rows:
        return 0
    for y in full_rows:
        for x in range(COLS):
            locked.pop((x, y), None)
    for y in reversed(full_rows):
        for (x, yk) in sorted(locked.copy(), key=lambda k: -k[1]):
            if yk < y:
                locked[(x, yk + 1)] = locked.pop((x, yk))
    return len(full_rows) * 10

def check_and_clear(locked):
    grid = create_grid(locked)
    points = clear_rows(grid, locked)
    return create_grid(locked), points

def check_game_over(locked):
    for (x, y) in locked:
        if y == 0:
            return True
    return False

def show_game_over():
    big_font = pygame.font.SysFont("Arial", 50)
    game_over_text = big_font.render("GAME OVER", True, (255, 255, 0))
    screen.blit(game_over_text, ((WIDTH - game_over_text.get_width()) // 2, HEIGHT // 2))
    pygame.display.update()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False

def main():
    locked = {}
    current_shape, current_color = generate_shape()
    current_pos = [COLS // 2, 0]
    move_delay = 100
    last_move_time = pygame.time.get_ticks()
    score = 0
    high_score = load_high_score()
    running = True

    while running:
        clock.tick(60)
        current_time = pygame.time.get_ticks()
        grid = create_grid(locked)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if current_time - last_move_time > move_delay:
            if keys[pygame.K_LEFT]:
                current_pos[0] -= 1
                if not is_valid(current_pos, current_shape, grid):
                    current_pos[0] += 1
                last_move_time = current_time
            elif keys[pygame.K_RIGHT]:
                current_pos[0] += 1
                if not is_valid(current_pos, current_shape, grid):
                    current_pos[0] -= 1
                last_move_time = current_time
            elif keys[pygame.K_DOWN]:
                current_pos[1] += 1
                if not is_valid(current_pos, current_shape, grid):
                    current_pos[1] -= 1
                    lock_shape(current_pos, current_shape, current_color, locked)
                    
                    grid, points = check_and_clear(locked)
                    score += points
                    
                    draw_grid(screen, grid, current_shape, current_color, current_pos, score, high_score)

                    if score > high_score:
                        high_score = score
                        save_high_score(high_score)
                    if check_game_over(locked):
                        draw_grid(screen, grid, current_shape, current_color, current_pos, score, high_score)
                        show_game_over()
                        running = False
                        break

                    current_shape, current_color = generate_shape()
                    current_pos = [COLS // 2, 0]

                last_move_time = current_time

        draw_grid(screen, grid, current_shape, current_color, current_pos, score, high_score)

    pygame.quit()

main()