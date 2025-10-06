# Day 2 - Tip Calculator Project Files

# 💰 Tip Calculator

A simple yet practical Python program that calculates how much each person should pay when splitting a bill with friends, including tip.

## 🎯 Project Overview

**Day:** 2/100  
**Course:** 100 Days of Code - Python Bootcamp by Dr. Angela Yu  
**Difficulty:** Beginner  
**Concepts Covered:** Data types, Type conversion, Mathematical operations, f-strings

## ✨ Features

- Calculate total bill amount including tip percentage
- Split the bill equally among multiple people
- Display the amount each person needs to pay
- Handles decimal precision (rounded to 2 decimal places)
- User-friendly input prompts

## 🚀 How It Works

1. User enters the total bill amount
2. User selects tip percentage (10%, 12%, or 15%)
3. User enters number of people splitting the bill
4. Program calculates and displays amount per person

## 💻 Sample Output

```
Welcome to the tip calculator!
What was the total bill? $150.00
How much tip would you like to give? 10, 12, or 15? 12
How many people to split the bill? 5
Each person should pay: $33.60
```

## 📊 Calculation Logic

```
Total Bill with Tip = Original Bill + (Original Bill × Tip Percentage)
Amount Per Person = Total Bill with Tip ÷ Number of People
```

**Example:**
- Bill: $150
- Tip: 12% = $18
- Total: $168
- Split between 5 people: $168 ÷ 5 = $33.60

## 🛠️ Technologies Used

- **Language:** Python 3.x
- **Concepts:** 
  - Type conversion (`int()`, `float()`)
  - Mathematical operators
  - String formatting (f-strings)
  - User input handling
  - Rounding functions

## 📝 Code Structure

```python
# 1. Get bill amount (float)
# 2. Get tip percentage (int)
# 3. Get number of people (int)
# 4. Calculate tip amount
# 5. Calculate total bill
# 6. Divide by number of people
# 7. Round to 2 decimal places
# 8. Display result
```

## 🎓 Learning Outcomes

By completing this project, I learned:

- ✅ How to work with different data types (int, float, string)
- ✅ Converting between data types using type casting
- ✅ Performing mathematical calculations in Python
- ✅ Using the `round()` function for decimal precision
- ✅ String formatting with f-strings
- ✅ Taking and processing user input
- ✅ Writing clean, readable code with comments

## 🔧 How to Run

1. Make sure Python 3.x is installed on your system
2. Download or clone this repository
3. Navigate to the `Day-02` folder
4. Run the program:
   ```bash
   python task.py
   ```
5. Follow the on-screen prompts

## 💡 Possible Enhancements

Future improvements I could add:
- [ ] Validate user input (handle negative numbers, zero division)
- [ ] Allow custom tip percentages
- [ ] Add currency formatting
- [ ] Include tax calculation option
- [ ] Save calculation history
- [ ] Create a GUI version

## 🐛 Known Issues

- Currently doesn't validate if user enters invalid input (non-numeric values)
- Assumes users will enter positive numbers
- Limited to predefined tip percentages

## 📚 Resources Used

- [100 Days of Code Course](https://www.udemy.com/course/100-days-of-code/)
- [Python Official Documentation](https://docs.python.org/3/)
- [Python round() function](https://docs.python.org/3/library/functions.html#round)

## 👨‍💻 Author

**Aabhas**  
B.Tech CSE (IT) - First Year  
Symbiosis University of Applied Sciences

Connect with me:
- GitHub: [https://github.com/Aabhas-Pal/python-100-days-challenge]
- LinkedIn: [https://www.linkedin.com/in/aabhas-pal-8181b3366/]

## 📅 Project Timeline

- **Started:** [05/10/2025]
- **Completed:** [06/10/2025]
- **Time Taken:** ~1 hour

## 🏆 Achievements

- ✅ Day 2/100 completed
- ✅ Understanding of Python data types
- ✅ First practical Python application
- ✅ Learned mathematical operations in Python

---

⭐ **Part of my #100DaysOfCode journey!**

[← Day 1: Band Name Generator](../Day-001) | [Day 3: Treasure Island →](../Coming Soon...)
```

**Date:** [06/10/25]  
**Day:** 2/100  
**Topic:** Data Types & Type Conversion  
**Time Spent:** ~1-1.5 hours

---

## 🎯 Today's Learning Objectives

- [x] Understand Python data types
- [x] Learn type conversion/casting
- [x] Work with mathematical operations
- [x] Use the round() function
- [x] Format strings with f-strings
- [x] Build a practical calculator application

---

## 📚 Key Concepts Learned

### 1. **Data Types in Python**

Python has several built-in data types. Today I learned about:

#### **String (str)**
```python
name = "Aabhas"
message = 'Hello World'
```
- Text data enclosed in quotes (single or double)
- Can concatenate with `+`
- Can multiply with `*` for repetition

#### **Integer (int)**
```python
age = 19
year = 2025
people = 5
```
- Whole numbers (positive or negative)
- No decimal points
- Used for counting, indexing

#### **Float (float)**
```python
price = 150.50
tip_percentage = 0.12
pi = 3.14159
```
- Numbers with decimal points
- More precise than integers
- Used for measurements, calculations

#### **Boolean (bool)**
```python
is_student = True
has_paid = False
```
- Only two values: `True` or `False`
- Used for conditions and logic (will learn more later)

---

### 2. **Type Checking**

Use `type()` to check data type:

```python
print(type(123))        # <class 'int'>
print(type(12.5))       # <class 'float'>
print(type("Hello"))    # <class 'str'>
print(type(True))       # <class 'bool'>
```

**Why this matters:** Understanding data types prevents errors in calculations and operations.

---

### 3. **Type Conversion (Type Casting)**

Converting between data types:

```python
# String to Integer
age = int("19")           # "19" → 19

# String to Float
bill = float("150.50")    # "150.50" → 150.5

# Integer to String
number = str(100)         # 100 → "100"

# Integer to Float
value = float(10)         # 10 → 10.0
```

**Real-world use in project:**
```python
bill = float(input("What was the total bill? $"))
# input() always returns string, so we convert to float
```

**Common Error:**
```python
# This won't work:
num = "123"
result = num + 10  # ❌ TypeError: can't concatenate str and int

# Fix:
num = int("123")
result = num + 10  # ✅ Works! Result = 133
```

---

### 4. **Mathematical Operations**

```python
# Basic operations
addition = 10 + 5        # 15
subtraction = 10 - 5     # 5
multiplication = 10 * 5  # 50
division = 10 / 5        # 2.0 (always returns float)

# Advanced operations
floor_division = 10 // 3  # 3 (removes decimal)
modulus = 10 % 3          # 1 (remainder)
exponent = 2 ** 3         # 8 (2 to the power of 3)
```

**Order of Operations (PEMDAS):**
- Parentheses
- Exponents
- Multiplication/Division
- Addition/Subtraction

```python
result = 2 + 3 * 4      # 14 (not 20)
result = (2 + 3) * 4    # 20 (parentheses first)
```

---

### 5. **The round() Function**

Used to round decimal numbers to specified precision:

```python
round(3.14159)           # 3 (rounds to nearest integer)
round(3.14159, 2)        # 3.14 (2 decimal places)
round(2.5)               # 2 (rounds to nearest even number)
round(3.5)               # 4
```

**In the project:**
```python
amount_per_person = round(total_with_tip / people, 2)
# Ensures money is displayed with exactly 2 decimal places
```

---

### 6. **f-Strings (Formatted String Literals)**

Modern way to format strings in Python 3.6+:

```python
name = "Aabhas"
age = 19

# Old way (don't use this):
message = "My name is " + name + " and I'm " + str(age)

# f-string way (use this!):
message = f"My name is {name} and I'm {age}"
```

**In the project:**
```python
print(f"Each person should pay: ${amount_per_person}")
```

**Advanced f-string formatting:**
```python
price = 150.5
print(f"Price: ${price:.2f}")  # Price: $150.50 (2 decimals)

name = "Aabhas"
print(f"Hello, {name.upper()}!")  # Hello, AABHAS!
```

---

## 💻 Project Breakdown: Tip Calculator

### **Step-by-Step Logic**

```python
# Step 1: Welcome message
print("Welcome to the tip calculator!")

# Step 2: Get bill amount (convert to float)
bill = float(input("What was the total bill? $"))

# Step 3: Get tip percentage (convert to int)
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

# Step 4: Get number of people (convert to int)
people = int(input("How many people to split the bill? "))

# Step 5: Calculate tip amount
tip_amount = bill * (tip / 100)

# Step 6: Calculate total with tip
total_with_tip = bill + tip_amount

# Step 7: Calculate amount per person
amount_per_person = total_with_tip / people

# Step 8: Round to 2 decimal places
final_amount = round(amount_per_person, 2)

# Step 9: Display result
print(f"Each person should pay: ${final_amount}")
```

### **Alternative Approach (More Concise)**

```python
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# One-line calculation
amount_per_person = round((bill * (1 + tip / 100)) / people, 2)

print(f"Each person should pay: ${amount_per_person}")
```

---

## 🤔 Challenges Faced

### **Challenge 1: Understanding Type Conversion**
**Problem:** Initially confused about when to use `int()` vs `float()`

**Solution:** 
- Use `int()` for whole numbers (number of people, tip percentage)
- Use `float()` for decimal numbers (bill amount, final calculation)

### **Challenge 2: Rounding Issues**
**Problem:** Results showed too many decimal places (33.6000000001)

**Solution:** Used `round(number, 2)` to limit to 2 decimal places

### **Challenge 3: Calculation Order**
**Problem:** Initially calculated tip incorrectly

**Solution:** 
- First: Calculate tip percentage as decimal (12% = 12/100 = 0.12)
- Then: Multiply by bill amount
- Finally: Add to original bill

---

## 💡 "Aha!" Moments

1. **f-strings are amazing!** Much cleaner than concatenation
2. **Type conversion is crucial** - `input()` always returns string
3. **Division always returns float** - even `10/5` gives `2.0`, not `2`
4. **Order of operations matters** - Use parentheses to be explicit

---

## 🔍 Real-World Applications

This project taught me skills useful for:
- Building financial calculators
- E-commerce checkout systems
- Point-of-sale (POS) systems
- Expense splitting apps (like Splitwise)
- Any application involving money calculations

---

## 📊 What I Can Build Now

With Day 1 + Day 2 knowledge, I can build:
- ✅ Simple calculators (add, subtract, multiply, divide)
- ✅ Unit converters (temperature, distance, currency)
- ✅ Age calculators
- ✅ BMI calculators
- ✅ Grade calculators
- ✅ Interest calculators

---

## 🎯 Practice Exercises I Could Try

1. **Temperature Converter**
   - Convert Celsius to Fahrenheit and vice versa
   - Formula: F = (C × 9/5) + 32

2. **BMI Calculator**
   - Input: weight (kg), height (m)
   - Calculate: BMI = weight / (height²)

3. **Simple Interest Calculator**
   - Input: principal, rate, time
   - Calculate: SI = (P × R × T) / 100

4. **Age in Days Calculator**
   - Input: age in years
   - Calculate: age × 365 days

---

## 📈 Progress Tracking

**Skills Gained:**
- [x] Understanding of Python data types
- [x] Type conversion mastery
- [x] Mathematical operations
- [x] String formatting with f-strings
- [x] Building practical applications

**Confidence Level:**
- Variables: ⭐⭐⭐⭐⭐
- Data Types: ⭐⭐⭐⭐⭐
- Type Conversion: ⭐⭐⭐⭐☆
- Math Operations: ⭐⭐⭐⭐⭐
- f-strings: ⭐⭐⭐⭐☆

---

## 🚀 Next Steps (Day 3 Preview)

Tomorrow I'll learn:
- Control flow (if/else statements)
- Conditional logic
- Comparison operators
- Nested conditions

**Excited to learn:** How to make programs that make decisions! 🎯

---

## 📝 Key Takeaways

1. **Always convert input data** - `input()` returns strings
2. **Choose the right data type** - int for whole numbers, float for decimals
3. **Use f-strings for formatting** - Cleaner and more readable
4. **Round money calculations** - Always 2 decimal places for currency
5. **Test with different inputs** - Make sure it works in all cases

---

## 💭 Personal Reflection

**What went well:**
- Understood data types quickly
- Project was practical and useful
- Code worked on first try after careful planning

**What was challenging:**
- Understanding when to use int vs float
- Remembering to convert input to correct type

**Time taken:** 1 hour (30 min learning + 30 min coding)

**Overall feeling:** Confident! Ready for Day 3! 💪

---

## 🔗 Useful Resources

- [Python Data Types - Official Docs](https://docs.python.org/3/library/stdtypes.html)
- [f-strings Guide](https://realpython.com/python-f-strings/)
- [Type Conversion Tutorial](https://www.w3schools.com/python/python_casting.asp)

---

**Day 2/100 Complete! ✅**

---

*These notes are part of my #100DaysOfCode journey. Follow along on [GitHub](https://github.com/Aabhas-Pal/python-100-days-challenge)!*
```
