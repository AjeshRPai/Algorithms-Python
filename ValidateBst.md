# Validate BST

### Question

Check if a Binary tree is valid or not. 

A Binary tree is valid 

1. IF the values on the left of the tree should be less than the root 

2. IF values on the right should be greater than or equal to the root. 

3. IF value is null or the child node are valid

For a root node 

right node value ≥ root value > left node value

### Solution

Do a recursion On the Tree and check for the Condition of 

```java
if(node==null)
        	return true;

if(node.value<minValue || node.value>=maxValue)
            return false;

return (isBstUtil(node.left,minValue,node.value)&&
                isBstUtil(node.right,node.value,maxValue));
```

### Time And Complexity Analysis

Time Complexity - O(number of nodes) - Since we have to iterate through the entire nodes

Space Complexity - O(depth of tree) - The entire tree values are mapped at an instance. One root is taken at first and then go to the depth of that node.