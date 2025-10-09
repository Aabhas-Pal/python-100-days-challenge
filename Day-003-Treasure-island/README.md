# Day 3 - Treasure Island Project Files

---


 🏴‍☠️ Treasure Island

An interactive text-based adventure game where players make choices to find hidden treasure while avoiding various dangers along the way.

## 🎯 Project Overview

**Day:** 3/100  
**Course:** 100 Days of Code - Python Bootcamp by Dr. Angela Yu  
**Difficulty:** Beginner  
**Concepts Covered:** Control Flow, Conditional Logic, if/elif/else statements, Nested conditions

## ✨ Features

- Interactive storytelling with player choices
- Multiple decision points affecting the outcome
- ASCII art title screen for visual appeal
- Various endings based on player decisions
- Simple yet engaging gameplay mechanics

## 🎮 How to Play

1. Run the program
2. Read the scenario and make choices
3. Type your choice exactly as prompted (case-sensitive)
4. Navigate through the story to find the treasure
5. Try different paths to discover all possible endings!

## 🗺️ Game Flow

```
START
  ↓
Crossroad (left/right)
  ↓
left → River (wait/swim)
  ↓
wait → Three Doors (red/yellow/blue)
  ↓
yellow → 🎉 WIN! (Treasure found!)
red → 💀 DEATH (Burned by flaming tiger)
blue → 💀 DEATH (Killed by leviathan)
  ↓
swim → 💀 DEATH (Eaten by piranhas)
  ↓
right → 💀 DEATH (Fell in sinkhole)
```

## 💻 Sample Gameplay


Welcome to Treasure Island.
Your mission is to find the treasure.
You are at a crossroad choose your path 
type left or right: left

You are in front of a river choose one option
wait for boat or swim.
wait

There are the doors in front of you choose one for treasure
red, yellow and blue what's your choice. 
yellow

Hurray! you got the treasure


## 🎯 All Possible Endings

| Choice Path | Outcome | Description |
|------------|---------|-------------|
| Right | 💀 Death | Fell in a sinkhole |
| Left → Swim | 💀 Death | Eaten by piranhas |
| Left → Wait → Red | 💀 Death | Burned by flaming tiger |
| Left → Wait → Blue | 💀 Death | Killed by leviathan |
| Left → Wait → Yellow | 🏆 Victory | Found the treasure! |

**Success Rate:** Only 1 winning path out of 5 possible endings (20%)

## 🛠️ Technologies Used

- **Language:** Python 3.x
- **Concepts:**
  - Conditional statements (if/elif/else)
  - Nested conditions
  - User input handling
  - String comparison
  - Multi-line strings (ASCII art)
  - Logical flow control

## 📝 Code Structure

```python
# 1. Display ASCII art title
# 2. Welcome message and mission briefing
# 3. First choice: Crossroad (left/right)
#    ├─ If right → Game Over (sinkhole)
#    └─ If left → Continue to river
# 4. Second choice: River (wait/swim)
#    ├─ If swim → Game Over (piranhas)
#    └─ If wait → Continue to doors
# 5. Third choice: Doors (red/yellow/blue)
#    ├─ If yellow → Victory!
#    ├─ If red → Game Over (tiger)
#    └─ If blue → Game Over (leviathan)
```

## 🎓 Learning Outcomes

By completing this project, I learned:

- ✅ How to use if/elif/else statements for decision-making
- ✅ Creating nested conditional statements (conditions within conditions)
- ✅ Building interactive narratives with code
- ✅ Controlling program flow based on user input
- ✅ Using comparison operators (==, !=)
- ✅ Understanding code indentation importance
- ✅ Creating engaging user experiences with simple tools

## 🔧 How to Run

1. Ensure Python 3.x is installed
2. Clone or download this repository
3. Navigate to the `Day-03` folder
4. Run the game:
   bash
   python task.py
   
5. Follow on-screen prompts and make your choices!

## 💡 Possible Enhancements

Future improvements I could add:

- [ ] Make choices case-insensitive (.lower())
- [ ] Add input validation (handle typos/invalid inputs)
- [ ] Include more story branches and choices
- [ ] Add ASCII art for different scenes
- [ ] Implement a scoring system
- [ ] Create multiple difficulty levels
- [ ] Add color to text output (using colorama)
- [ ] Include inventory system
- [ ] Add save/load game feature
- [ ] Create a restart option without re-running

## 🎨 Creative Elements

### ASCII Art
The game features a custom treasure island ASCII art created with:
```python
print(r'''
[ASCII art goes here]
''')
```
The `r` prefix creates a raw string, preserving all special characters and formatting.

### Story Writing
Each outcome has a unique, creative description:
- 🌊 Piranhas: "A bunch of hungry piranha's fed upon you."
- 🔥 Tiger: "You burned crisp fighting with a flaming tiger."
- 🐉 Leviathan: "You died while fighting with leviathan."
- 🕳️ Sinkhole: "You died falling in a sink hole."
- 🏆 Treasure: "Hurray! you got the treasure"

## 🐛 Known Issues

- **Case-sensitive inputs:** Typing "Left" instead of "left" will cause unexpected behavior
- **No input validation:** Invalid inputs (typos) aren't handled gracefully
- **No replay option:** Must restart program to play again

### Planned Fixes:
```python
# Future improvement example:
choice = input("Type left or right: ").lower()
# This makes input case-insensitive
```

## 🎮 Game Design Insights

**Why the winning path is challenging:**
- Multiple decision points reduce success probability
- No hints about correct choices (discovery through exploration)
- Creative death scenarios encourage replaying

**Player Psychology:**
- Most players naturally choose "left" (unconscious bias)
- "Wait" feels safer than "swim" (patience rewarded)
- Yellow is often associated with gold/treasure

## 📚 Resources Used

- [100 Days of Code Course](https://www.udemy.com/course/100-days-of-code/)
- [Python if/else - Official Docs](https://docs.python.org/3/tutorial/controlflow.html)
- [ASCII Art Generator](http://patorjk.com/software/taag/)

## 👨‍💻 Author

**Aabhas**  
B.Tech CSE (IT) - First Year  
Symbiosis University of Applied Sciences

Connect with me:
- GitHub: [https://github.com/Aabhas-Pal/python-100-days-challenge]
- LinkedIn: [https://www.linkedin.com/in/aabhas-pal-8181b3366/]

## 📅 Project Timeline

- **Started:** [08/10/2025]
- **Completed:** [09/10/2025]
- **Time Taken:** ~1.5 hours

## 🏆 Achievements

- ✅ Day 3/100 completed
- ✅ First interactive game created
- ✅ Mastered nested conditionals
- ✅ Implemented branching story logic
- ✅ Created engaging user experience

---

⭐ **Part of my #100DaysOfCode journey!**

[← Day 2: Tip Calculator](../Day-02) | [Day 4: Rock Paper Scissors →](../Day-04)
```

---

