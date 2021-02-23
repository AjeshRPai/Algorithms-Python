# Add Binary

### **Question**

Given two binary strings (strings containing only 1s and 0s) return their sum (also as a binary string).

Note: neither binary string will contain leading 0s unless the string itself is 0

### **Sample input/Output:**

Input:  "100" + "1",  

Output: "101"

Input : "11" + "1", 

Output: "100", 

Input: "1" + "0"

Output: "1"

### **Boundary Conditions**

1. The String will contain only 0 s and 1s 
2. The String will not contain leading 0's unless the String itself is 0

### **Pseudocode**

1. Make the length of both the Strings equal. Maximum of two can be taken 
2. Then Starting from the right traverse to left 
3. Keep a variable to Check for Carry also 
4. If  1 + 1 . then result 0 and carry 1
5. if  1 + 0 = 1
6. Note **Spill over Scenario**: If the carry ≠0 and Traversal is finished then Add one more string with "1" value .

### **Solution**

```python
current_sum = carry

if first_string[i] == '1':
    current_sum += 1
else:
    current_sum += 0

if second_string[i] == '1':
    current_sum += 1
else:
    current_sum += 0

if current_sum == 1:
    sum = "1" + sum
    carry =0
elif current_sum == 2:
    sum = "0" + sum
    carry = 1
elif current_sum == 3:
    sum = "1" + sum
    carry = 1
else:
    sum = "0" + sum
    carry = 0

if carry != 0 and i == 0:
    sum = "1"+sum
```