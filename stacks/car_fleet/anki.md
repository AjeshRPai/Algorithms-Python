### Anki Flash Card: Key Points to Solve the "Car Fleet" Problem

#### Front

What are the key points to solve the "Car Fleet" problem?

#### Back

1. **Sort Cars by Position**:
    - Sort cars in descending order of position so the closest car to the target is processed first.

2. **Fleet Formation**:
    - A fleet forms when a car behind takes less or equal time to reach the target than the car in front. The cars merge
      into a single fleet.

3. **Calculate Time to Reach Target**:
    - For each car, calculate the time to reach the target using `(target - position) / speed`.

4. **Use a Stack**:
    - A stack is used to track the time each fleet will take to reach the target. If a car’s time is less than or equal
      to the previous fleet, they merge. The number of fleets is the size of the stack at the end.