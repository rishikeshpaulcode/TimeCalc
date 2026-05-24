# Time Calculation Library

Project: Time Calculation Library build using python

---

## Features

1. Addition of time with time.
2. Substraction of time with time.
3. Division of time with time.
4. Division of time with scalar.
5. Multiplication of time with scalar.

---

## Keywords

1. **exit**: terminates the program
2. **now**: returns current time
3. **ans**: return the result of previous expression
4. **rand**: generates a random timestamp

---

## Operators

1. `+` : addition
2. `-` : substraction
3. `/` : division
4. `*` : multiplication
5. `>>` : returns time in between two timestamps
6. `==` : returns true if the two timestamps are same else false
7. `!=` : returns true if the two timestamps are not same else false
8. `<` : returns true when LHS time is less than RHS time else false
9. `<=` : returns true when LHS time is less than or equal to RHS time else false
10. `>` : returns true when LHS time is greater than RHS time else false
11. `>=` : returns true when LHS time is greater than or equal to RHS time else false

---

## Exceptions

1. **ParsingError**: something went wrong while creating time object
    - **a. NullValueError**: no value was passed for creation of time object
    - **b. FormatError**: invalid format of time passed for creation of time object
2. **CalculationError**: something went wrond while performing some operation
    - **a. InvalidOperandError**: operation with passed operand(s) in not defined
    - **b. ZeroDivisionError**: dividing time by zero is not defined

---

## Program Flow

1. **Display Title**
2. **Loop**:
    - **a.** Accept an expression from user (it may contain any number of tokens)
    - **b.** convert the expression into list of tokens
    - **c.** parse the tokens as per its type (if 'exit' is encountered, break the loop)
    - **d.** evaluate the final string of tokens using custom dunder methods
    - **e.** display and save result, reset initial state
    
    > **Note:** stop loop if error occurs in any step, display error message and continue with next iteration
3. **terminate program**

---

## Installation

You can install this library directly from GitHub using `pip`:
> pip install git+https://github.com/rishikeshpaulcode/TimeCalc.git

---

## Clone the Repository

1. **Using HTTPS**:
    > git clone https://github.com/rishikeshpaulcode/TimeCalc.git
2. **Using GitHub CLI**:
    > gh repo clone rishikeshpaulcode/TimeCalc
