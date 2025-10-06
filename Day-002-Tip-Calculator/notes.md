# Notes - Day 2 (Tip Calculator) 💰

## 🧠 Project Overview
The **Tip Calculator** is a simple Python project that helps users calculate how much each person should pay when splitting a restaurant bill, including the tip amount.

This project is part of **Day 2** of the *100 Days of Code: Python Challenge*.

---

## ✅ What I Learned
- How to **take user input** using the `input()` function.  
- How to **convert string input to numeric types** using `int()` and `float()`.  
- Basic **arithmetic operations** in Python.  
- How to **format output** using f-strings (`f"{}"`).  
- The importance of **operator precedence** when performing calculations.

---

## 🧩 Key Concepts Practiced
| Concept | Description |
|----------|--------------|
| `input()` | To take data from the user |
| `float()` & `int()` | Type conversion for mathematical operations |
| Arithmetic Operators | Used for calculating tips and totals |
| f-Strings | Formatting the output message cleanly |

---

## 💡 Mistakes Noticed & Fixes
1. ⚠️ **Incorrect Formula for Total Calculation**  
   - In your code:  
     ```python
     total = ((bill / 5) * net_tip) / people
     ```
     Here `/5` was mistakenly dividing the bill by 5 instead of using the total bill amount.  
   - ✅ **Correct Formula:**  
     ```python
     total = (bill * net_tip) / people
     ```

2. 💬 Always check if the tip percentage is added correctly using:  
   ```python
   net_tip = (tip / 100) + 1
