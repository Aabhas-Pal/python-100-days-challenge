# ✊✋✌️ Rock Paper Scissors Game

A classic Rock Paper Scissors game implemented in Python, featuring ASCII art visuals and random computer opponent. Play against the computer and test your luck!

## 🎯 Project Overview

**Day:** 4/100  
**Course:** 100 Days of Code - Python Bootcamp by Dr. Angela Yu  
**Difficulty:** Beginner  
**Concepts Covered:** Lists, Random module, Indexing, Game logic, Conditional statements

## ✨ Features

- Interactive command-line gameplay
- ASCII art representations of rock, paper, and scissors
- Randomized computer opponent
- Input validation for invalid choices
- Multiple game outcomes (Win/Lose/Draw)
- Clear visual feedback for both player and computer choices

## 🎮 How to Play

1. Run the program
2. Choose your move:
   - Type `0` for Rock ✊
   - Type `1` for Paper ✋
   - Type `2` for Scissors ✌️
3. Computer makes its random choice
4. Winner is determined by classic rules:
   - Rock beats Scissors
   - Scissors beats Paper
   - Paper beats Rock
   - Same choice = Draw

## 🎲 Game Rules

| Player | Computer | Result |
|--------|----------|--------|
| Rock (0) | Scissors (2) | **Player Wins** 🎉 |
| Rock (0) | Paper (1) | Computer Wins 😢 |
| Paper (1) | Rock (0) | **Player Wins** 🎉 |
| Paper (1) | Scissors (2) | Computer Wins 😢 |
| Scissors (2) | Paper (1) | **Player Wins** 🎉 |
| Scissors (2) | Rock (0) | Computer Wins 😢 |
| Any | Same | **Draw** 🤝 |

## 💻 Sample Gameplay
                    Welcome to the rock paper and scissors game
What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.
0
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
Computer chose:
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
You lose!
Thanks for playing with us!!!

## 🛠️ Technologies Used

- **Language:** Python 3.x
- **Modules:** 
  - `random` - For generating computer's random choice
- **Concepts:**
  - Lists and list indexing
  - Random number generation (`random.randint()`)
  - Multi-line strings (ASCII art)
  - Conditional logic (if/elif/else)
  - Input validation
  - Comparison operators

## 📝 Code Structure
```python
# 1. Import random module
# 2. Display welcome message
# 3. Define ASCII art for rock, paper, scissors
# 4. Store options in a list
# 5. Get user input (0, 1, or 2)
# 6. Display user's choice with ASCII art
# 7. Generate computer's random choice
# 8. Display computer's choice with ASCII art
# 9. Validate user input
# 10. Compare choices and determine winner
# 11. Display result
```

## 🎓 Learning Outcomes

By completing this project, I learned:

- ✅ How to use Python's `random` module
- ✅ Working with lists and accessing elements by index
- ✅ List indexing syntax (`list[0]`, `list[1]`, etc.)
- ✅ Generating random integers with `random.randint()`
- ✅ Implementing game logic with multiple conditions
- ✅ Input validation and error handling
- ✅ Creating engaging CLI experiences with ASCII art
- ✅ Understanding modular code organization

## 🔧 How to Run

1. Ensure Python 3.x is installed on your system
2. Clone or download this repository
3. Navigate to the `Day-04` folder
4. Run the game:
```bash
   python task.py
```
5. Enter your choice (0, 1, or 2) and press Enter
6. See the result and play again by re-running!

## 💡 Code Highlights

### **List for Game Options**
```python
game_options = [rock, paper, scissors]
# Accessing: game_options[0] = rock
#            game_options[1] = paper  
#            game_options[2] = scissors
```

### **Random Computer Choice**
```python
computer_choice = random.randint(0, 2)
# Generates random number: 0, 1, or 2
```

### **Input Validation**
```python
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
```

### **Win Condition Logic**
```python
# Player wins scenarios
if user_choice == 0 and computer_choice == 2:  # Rock beats Scissors
    print("You win!")
elif user_choice == 1 and computer_choice == 0:  # Paper beats Rock
    print("You win!")
elif user_choice == 2 and computer_choice == 1:  # Scissors beats Paper
    print("You win!")
```

## 🎨 ASCII Art

The game features hand-crafted ASCII art for each choice:

- **Rock (0):** Closed fist ✊
- **Paper (1):** Open hand ✋
- **Scissors (2):** Victory sign ✌️

## 💡 Possible Enhancements

Future improvements I could add:

- [ ] Add score tracking (best of 3, best of 5)
- [ ] Create a replay option without restarting
- [ ] Add difficulty levels (predictable AI patterns)
- [ ] Include "Rock Paper Scissors Lizard Spock" variant
- [ ] Add color to output using `colorama` library
- [ ] Create animated ASCII art
- [ ] Add sound effects
- [ ] Implement multiplayer mode
- [ ] Save high scores to a file
- [ ] Add tournament mode

## 🐛 Known Issues & Edge Cases

### **Current Limitations:**
1. **Non-integer input:** Entering letters causes a crash
```python
   # Future fix:
   try:
       user_choice = int(input("Choose: "))
   except ValueError:
       print("Please enter a number!")
```

2. **No replay option:** Must restart program to play again
```python
   # Future fix: wrap in while loop
   play_again = "yes"
   while play_again == "yes":
       # game code here
       play_again = input("Play again? (yes/no): ")
```

3. **ASCII art alignment:** May look different on some terminals

### **What Works Well:**
- ✅ Proper input validation for out-of-range numbers
- ✅ Clear win/lose/draw logic
- ✅ Random computer opponent (fair gameplay)
- ✅ Visual feedback with ASCII art

## 🎲 Game Statistics

**Probability Analysis:**
- Each option has 33.33% chance (fair RNG)
- Win probability: 33.33%
- Lose probability: 33.33%
- Draw probability: 33.33%

**Total Possible Outcomes:** 9 combinations (3 × 3)

## 🧮 Game Logic Breakdown

### **Win Conditions (3 scenarios):**
1. Rock (0) vs Scissors (2) → Player wins
2. Paper (1) vs Rock (0) → Player wins
3. Scissors (2) vs Paper (1) → Player wins

### **Lose Conditions (3 scenarios):**
1. Rock (0) vs Paper (1) → Computer wins
2. Paper (1) vs Scissors (2) → Computer wins
3. Scissors (2) vs Rock (0) → Computer wins

### **Draw Condition (3 scenarios):**
1. Rock (0) vs Rock (0)
2. Paper (1) vs Paper (1)
3. Scissors (2) vs Scissors (2)

## 📚 Resources Used

- [100 Days of Code Course](https://www.udemy.com/course/100-days-of-code/)
- [Python Random Module](https://docs.python.org/3/library/random.html)
- [Python Lists Tutorial](https://docs.python.org/3/tutorial/datastructures.html)
- [ASCII Art Archive](https://www.asciiart.eu/)

## 👨‍💻 Author

**Aabhas**  
B.Tech CSE (IT) - First Year  
Symbiosis University of Applied Sciences

> "Hey guys welcome to my journey of python programming! This is the fourth project ever created. Please stay tuned for upcoming projects." 🚀

Connect with me:
- GitHub: [https://github.com/Aabhas-Pal]
- LinkedIn: [https://www.linkedin.com/in/aabhas-pal-8181b3366/]

## 📅 Project Timeline

- **Started:** [16/10/2025]
- **Completed:** [17/10/2025]
- **Time Taken:** ~1.5 hours

## 🏆 Achievements

- ✅ Day 4/100 completed
- ✅ First game with randomization
- ✅ Learned list data structure
- ✅ Implemented random module
- ✅ Created fair game logic
- ✅ **Streak: 4 days!** 🔥🔥🔥🔥

---

⭐ **Part of my #100DaysOfCode journey!**

[← Day 3: Treasure Island](../Day-03) | [Day 5: Password Generator →](../Day-05)
