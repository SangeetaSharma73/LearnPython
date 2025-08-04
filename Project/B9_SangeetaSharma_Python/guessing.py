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
