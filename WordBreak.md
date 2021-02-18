# Word Dictionary / Word Break

### **Question**

Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].

### **Sample input/Output:**

**Input**:'quick', 'brown', 'the', 'fox', and the word "thequickbrownfox", 

**Expected Output**: ['the', 'quick', 'brown', 'fox'].

### **Boundary Conditions**

1. Nothing common in both the input
2. If multiple words are common 

Example: 'bed', 'bath', 'bedbath', 'and', 'beyond' and **string** "bedbathandbeyond"

### **Pseudocode**

1. Out of the Both Inputs. String and Array of words. Take String and iterate/recurse by each letter 
2. The iteration will have to be done by taking each letter and combining the rest of the word 
3. So in total two passes will be required. One iteration for taking the first letter and Second iteration for adding rest of the letters one by one 

### **Solution**

```python
for i in range(0, len(str)):
        first_letter = str[i]

        if first_letter in dict:
            output_array.append(first_letter)

        rest_of_the_letters = str[i + 1:]
        for j in range(1, len(rest_of_the_letters) + 1):
            rest_of_letter = rest_of_the_letters[:j]
            possible_match = first_letter + rest_of_letter
            print(possible_match)
            if possible_match in dict:
                output_array.append(possible_match)
```