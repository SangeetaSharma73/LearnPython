# 🧱 Falling Block Game – Code Structure & Explanation

## 1. Game Setup

- **Imports:**
  - `pygame`: Game library.
  - `random`: Generates random shapes and colors.
  - `os`: Checks if the high score file exists.

---

## 2. Game Constants and Initialization

```python
ROWS, COLS = 10, 10  # Game grid size
BLOCK_SIZE = 40      # Each block is 40x40 pixels
WIDTH, HEIGHT = COLS * BLOCK_SIZE, ROWS * BLOCK_SIZE
TOP_MARGIN = 40      # Space for the score display

COLORS = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255),
    (255, 255, 0), (255, 0, 255), (0, 255, 255)
]
```

- Defines the game board, block size, and block colors.

```python
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT + TOP_MARGIN))
pygame.display.set_caption("Falling Block Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)
```

- Initializes Pygame, sets up the screen, title, and font.

---

## 3. High Score Functions

```python
high_score_file = "highscore.txt"

def load_high_score():
    if os.path.exists(high_score_file):
        with open(high_score_file, 'r') as f:
            return int(f.read())
    return 0

def save_high_score(score):
    with open(high_score_file, 'w') as f:
        f.write(str(score))
```

- Reads and writes the high score from/to a file.

---

## 4. Grid Setup

```python
def create_grid(locked={}):
    grid = [[(0, 0, 0) for _ in range(COLS)] for _ in range(ROWS)]
    for (x, y), color in locked.items():
        if y >= 0:
            grid[y][x] = color
    return grid
```

- Creates a 2D grid of the board.
- Locked positions (previously fallen blocks) are shown in the grid.

---

## 5. Drawing Function

```python
def draw_grid(surface, grid, current_shape, current_color, current_pos, score, high_score):
    ...
```

- Draws the entire game scene:
  - Score and High Score at the top.
  - Game grid and falling shape.
  - Grid lines for better visuals.

---

## 6. Shape Generator

```python
def generate_shape():
    ...
```

- Randomly creates a shape with 1–4 blocks, connected like in Tetris.
- Uses a flood-fill-like method to create organic shapes.

---

## 7. Collision Check Function

```python
def is_valid(pos, shape, grid):
    for dx, dy in shape:
        x = pos[0] + dx
        y = pos[1] + dy
        if x < 0 or x >= COLS or y >= ROWS:
            return False
        if y >= 0 and grid[y][x] != (0, 0, 0):
            return False
    return True
```

- Checks if the shape at its new position:
  - Is inside the grid.
  - Does not collide with other locked blocks.

---

## 8. Utility Functions

```python
def get_block_positions(pos, shape):
    return [(pos[0] + dx, pos[1] + dy) for dx, dy in shape]

def lock_shape(pos, shape, color, locked):
    for x, y in get_block_positions(pos, shape):
        if y >= 0:
            locked[(x, y)] = color
```

- `get_block_positions`: Returns actual grid coordinates for each part of the shape.
- `lock_shape`: Locks the current shape into the grid when it hits the bottom or another block.

---

## 9. Clearing Full Rows

```python
def clear_rows(grid, locked):
    ...
```

- Checks for rows that are completely filled.
- Clears them and moves the blocks above down.
- Returns the score earned from clearing rows.

```python
def check_and_clear(locked):
    grid = create_grid(locked)
    points = clear_rows(grid, locked)
    return create_grid(locked), points
```

- Wrapper to update grid and score after clearing rows.

---

## 10. Game Over Check

```python
def check_game_over(locked):
    for (x, y) in locked:
        if y == 0:
            return True
    return False

def show_game_over():
    ...
```

- If any locked block is in the top row, the game is over.
- Displays “Game Over” on the screen until the player closes the window.

---

## 11. Main Game Loop

```python
def main():
    ...
    locked = {}
    current_shape, current_color = generate_shape()
    current_pos = [COLS // 2, 0]  # Shape starts in middle top
    ...
    while running:
        clock.tick(60)  # Runs at 60 frames per second
        ...
        keys = pygame.key.get_pressed()
        # Handle Movement
        if keys[pygame.K_LEFT]:
            current_pos[0] -= 1
            if not is_valid(current_pos, current_shape, grid):
                current_pos[0] += 1
        elif keys[pygame.K_RIGHT]:
            current_pos[0] += 1
            if not is_valid(current_pos, current_shape, grid):
                current_pos[0] -= 1
        elif keys[pygame.K_DOWN]:
            current_pos[1] += 1
            if not is_valid(current_pos, current_shape, grid):
                current_pos[1] -= 1
                lock_shape(...)
                ...
        # Final Drawing
        draw_grid(...)
    pygame.quit()
```

- Handles initialization, movement, collision, locking, clearing rows, game over, and drawing.
- Continuously updates the screen with new positions.
- Exits cleanly when
