### 4. Anki Flash Card Based on Key Points

#### Front

What data structure is used to solve the "daily temperatures" problem, and how does it help?

#### Back

A **monotonic stack** is used, which helps keep track of indices of temperatures in decreasing order. This allows the
function to efficiently compute how many days one needs to wait for a warmer temperature.

---

#### Front

When do you update the result for a temperature in the "daily temperatures" problem?

#### Back

The result is updated when the current temperature is warmer than the temperature at the top of the stack. The index
difference between the current day and the popped day is the number of days to wait.

---

#### Front

What happens if there is no future warmer day for a temperature in the "daily temperatures" problem?

#### Back

If there is no future warmer day, the corresponding entry in the result list remains `0`.

---

#### Front

What is the time complexity of the solution for the "daily temperatures" problem?

#### Back

The time complexity is `O(n)` because each temperature is pushed and popped from the stack at most once.