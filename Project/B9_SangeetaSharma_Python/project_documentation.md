# 🕹️ Animal Guessing Game

## 👦 Author

**Sangeeta Sharma**

---

## 🎯 Objective

To develop a Python console-based game that:

- Selects a random animal from a list.
- Gives three fun hints to help the player guess the animal.
- Checks if the guess is correct.
- Congratulates the user on success or reveals the correct answer.

---

## 🧰 Technologies Used

| Component       | Purpose                  |
| --------------- | ------------------------ |
| Python          | Programming language     |
| random          | To pick a random animal  |
| print()/input() | For console input/output |

---

## 📜 Project Description

This project is a beginner-level educational guessing game designed to help players learn basic Python programming and logical thinking. Players read clues about an animal and try to guess which one it is.

---

## 🔧 How It Works

1. A list of animals is stored with 3 hints each.
2. The computer randomly picks one animal.
3. The player sees the 3 hints and enters their guess.
4. If correct: A congratulations message is shown.
5. If incorrect: The program shows the right answer.
6. The game ends after one guess (can be enhanced to allow retries).

---

## 💻 Code

```python
# Animal Guessing Game for 6th Grade

# List of animals and their hints
animals = {
    "elephant": ["I am the largest land animal.", "I have a trunk.", "I love peanuts!"],
    "lion": ["I am the king of the jungle.", "I roar loud!", "I have a golden mane."],
    "penguin": ["I cannot fly.", "I waddle on ice.", "I live in Antarctica."],
    "giraffe": ["I have a long neck.", "I eat leaves from tall trees.", "I am the tallest land animal."],
    "monkey": ["I swing on trees.", "I eat bananas.", "I love playing tricks!"]
}

import random

# Choose a random animal
animal, hints = random.choice(list(animals.items()))

print("🐾 Welcome to the Animal Guessing Game!")
print("Can you guess the animal based on these 3 hints?\n")

# Show hints
for i, hint in enumerate(hints):
    print(f"Hint {i+1}: {hint}")

# Get user's guess
guess = input("\nWhat animal am I? ").strip().lower()

# Check answer
if guess == animal:
    print("🎉 Correct! You guessed the animal!")
else:
    print(f"❌ Oops! The correct answer was '{animal.title()}'. Try again next time!")
```

---

## 🖥️ Sample Output

```
🐾 Welcome to the Animal Guessing Game!
Can you guess the animal based on these 3 hints?

Hint 1: I swing on trees.
Hint 2: I eat bananas.
Hint 3: I love playing tricks!

What animal am I? monkey
🎉 Correct! You guessed the animal!
```

---

## 🌟 Possible Enhancements

- Allow multiple guesses or limited tries (like 3 chances).
- Track score for multiple rounds.
- Add difficulty levels (easy: common animals, hard: rare ones).
- Add fun animal sounds using the `pygame` or `playsound` library.
- Add graphics with `pygame` to show animal pictures after guessing.

---

## 🏁 Conclusion

This project is perfect for young learners who are beginning their Python journey. It teaches:

- How to use dictionaries and lists
- How to take input from the user
- Basic condition checking (`if-else`)
- Use of randomness for variety

It’s fun, educational, and easy to extend as coding skills grow!

---
