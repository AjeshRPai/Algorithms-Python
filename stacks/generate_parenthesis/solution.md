### Key Points to Memorize the Solution

1. **Backtracking:**
    - The solution uses backtracking to explore all possible combinations of valid parentheses.

2. **Base Condition:**
    - When the number of open and close parentheses equals `n`, a valid combination is formed and stored.

3. **Recursive Conditions:**
    - You can add an open parenthesis `(` if the number of open parentheses is less than `n`.
    - You can add a close parenthesis `)` if the number of close parentheses is less than the number of open
      parentheses, ensuring valid sequences.

4. **Stack for Tracking:**
    - The stack stores the current sequence of parentheses being built.

5. **Exploration and Backtracking:**
    - After adding a parenthesis, the function explores further possibilities, and when it's done, it removes the last
      parenthesis to explore alternative paths.

### 4. Anki Flash Cards

#### Front

What technique is used to generate all valid parentheses in the solution?

#### Back

Backtracking is used to explore all possible combinations of valid parentheses by making decisions at each step and
undoing them if necessary.

---

#### Front

What is the base condition in the parentheses generation solution?

#### Back

The base condition is when the number of open and close parentheses both equal `n`. At this point, a valid combination
is formed and added to the result.

---

#### Front

When can an open parenthesis be added in the parentheses generation solution?

#### Back

An open parenthesis can be added if the number of open parentheses is less than `n`.

---

#### Front

When can a close parenthesis be added in the parentheses generation solution?

#### Back

A close parenthesis can be added if the number of close parentheses is less than the number of open parentheses,
ensuring the sequence remains valid.

---

#### Front

How does backtracking help in generating valid parentheses?

#### Back

Backtracking allows the function to explore a decision (like adding a parenthesis), then undo it (remove the
parenthesis) to explore other possibilities.