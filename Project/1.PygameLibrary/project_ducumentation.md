# 🕹️ Project Name

**Catch the Falling Fruit** Game

## 🧑 Author

Sangeeta Sharma

## 🎯 Objective

To develop a beginner-friendly graphical game using Python and Pygame where:

- 🍎 Fruits fall from the top of the screen.
- 🧺 The player moves a basket left or right to catch them.
- 🏆 The score increases with each successful catch.
- 💡 The game promotes logic-building and game development skills in Python.

## 🧰 Technologies Used

| Technology | Purpose                                    |
| ---------- | ------------------------------------------ |
| Python     | Programming language                       |
| Pygame     | Game development (graphics, events, input) |
| Random     | Generate random fruit positions            |

## 📜 Project Description

This project is a beginner-level 2D arcade-style game that introduces players to real-time game loops, keyboard control, object collision, and scorekeeping using Python.

## 🚦 How It Works

- The game window is initialized using pygame.
- A basket is drawn at the bottom of the screen.
- A fruit falls from the top at random positions.
- The player uses the arrow keys to move the basket.
- If the fruit touches the basket, the player earns a point.
- The game continues in a loop until the player exits.

## 🧑‍💻 Code Summary

**Screen Setup:**

```python
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
```

**Basket Logic:**

```python
basket_x -= basket_speed  # Move left
basket_x += basket_speed  # Move right
```

**Fruit Generation & Movement:**

```python
fruit_x = random.randint(0, WIDTH - fruit_radius)
fruit_y += fruit_speed
```

**Collision Detection:**

```python
if basket_y < fruit_y + fruit_radius < basket_y + basket_height and basket_x < fruit_x < basket_x + basket_width:
    score += 1
```

**Score Display:**

```python
score_text = font.render(f"Score: {score}", True, (0, 0, 0))
```

## 🖥️ Sample Output (What You See)

- A white game window with:
  - 🧺 A brown basket at the bottom.
  - 🍎 Red fruit falling from the top.
  - 🏆 Score displayed in the top-left.
- Player moves basket with arrow keys.
- Points increase as fruits are caught.

## 🌟 Possible Enhancements

- ✅ Add sound effects and background music.
- ✅ Use image assets for fruits and basket instead of basic shapes.
- ✅ Introduce levels with increasing fruit speed.
- ✅ Add timer or lives for challenge.
- ✅ Display a “Game Over” screen when lives are lost.
- ✅ Store and display high scores.

## 🏁 Conclusion

This project is a fun and engaging introduction to game development with Python. It teaches:

- Graphics rendering
- Event handling
- Collision detection
- Game loop mechanics

It’s a great foundation for making more advanced games like car racers, flappy bird clones, or even multiplayer games in the
