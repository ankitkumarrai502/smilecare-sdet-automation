# Week 1 · Day 1 — Python Basics (absolute zero start)

Time budget: ~2-2.5 hrs. Do this in VS Code. Open this folder (`SmileCare-SDET-Automation`) in VS Code, open a terminal inside it (`` Ctrl+` ``).

## 0. Sanity-check your setup (5 min)

In the VS Code terminal:

```bash
python --version
```

You should see `Python 3.x.x`. If you get an error, tell me before continuing — everything else depends on this working.

## 1. What is a Python script? (10 min)

A `.py` file is just a text file full of instructions Python reads top-to-bottom and executes. Create `learning/week01/scratch.py` and type:

```python
print("Hello, SmileCare")
```

Run it from the terminal:

```bash
python learning/week01/scratch.py
```

You should see `Hello, SmileCare` printed. `print()` is a **function** — a reusable block of behavior you call by writing its name followed by parentheses containing whatever it needs (here, the text to display).

## 2. Variables & data types (30 min)

A variable is a labeled box that holds a value.

```python
product_name = "Paracetamol 500mg"   # str (text) — always in quotes
price = 49.99                         # float (decimal number)
stock_count = 120                     # int (whole number)
in_stock = True                       # bool (True/False)
```

Python figures out the type automatically (this is called "dynamic typing"). Check any variable's type:

```python
print(type(price))     # <class 'float'>
```

**Why this matters for testing:** every field you'll see in the SmileCare API (`name`, `price`, `stock`, `verified`) is one of these same basic types. When you write an API test later, you're literally asserting "is this field the type and value I expect?"

### String basics

```python
first = "Amoxicillin"
strength = "250mg"
full_name = first + " " + strength          # "concatenation" -> Amoxicillin 250mg
full_name_f = f"{first} {strength}"         # f-string — the modern, preferred way
print(full_name_f)
print(full_name_f.upper())     # AMOXICILLIN 250MG
print(len(full_name_f))        # number of characters
```

### Numbers & operators

```python
price = 49.99
quantity = 3
subtotal = price * quantity
print(subtotal)              # 149.97
print(subtotal > 100)        # True  (comparison -> gives a bool)
print(round(subtotal, 1))    # 150.0
```

Operators: `+ - * /` (math), `//` (whole-number division), `%` (remainder), `== != > < >= <=` (comparisons), `and or not` (logic).

## 3. Getting input & basic control flow (25 min)

```python
category = input("Enter a category name: ")

if category == "Antibiotics":
    print("Prescription required")
elif category == "Pain Relief":
    print("Over the counter")
else:
    print("Category not recognized")
```

`if / elif / else` lets your program make decisions — this is the backbone of every test assertion you'll ever write ("if the response status is 200, pass; otherwise, fail").

**Indentation is not style in Python — it's syntax.** The 4 spaces under `if` define what belongs to that block. Getting this wrong is the #1 beginner error.

## 4. Comments (2 min)

```python
# This is a comment. Python ignores this line entirely.
price = 49.99  # inline comments explain "why", not "what"
```

## 5. Today's exercises (45-60 min)

Open `learning/week01/day01_exercises.py` — it has 5 TODOs. Do them in order, run the file after each one to check your output. Don't peek at `day01_solutions.py` until you've genuinely tried.

## 6. Wrap up (10 min)

Commit today's work:

```bash
git add .
git commit -m "week1 day1: python basics - variables, types, if/else"
git push
```

(If you haven't done `git init` / created the GitHub repo yet, see the root `README.md` "Pushing this to your own GitHub" section first.)

**Tomorrow (Day 2):** loops, lists, dictionaries, and functions — you'll build a tiny Python model of a SmileCare shopping cart.
