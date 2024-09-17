### Visualization for Anki Cards

Here are the key points broken down into Anki-style questions and answers:

1. **Using a Dummy Node:**
    - **Front:** Why use a dummy node in the `removeNthFromEnd` function?
    - **Back:** A dummy node simplifies edge cases, especially when removing the head node, by providing a consistent
      previous node for manipulation.

2. **Advancing the Right Pointer:**
    - **Front:** How does advancing the `right` pointer by `n` steps help in the `removeNthFromEnd` function?
    - **Back:** It ensures that `left` and `right` maintain a gap of `n` nodes, allowing `left` to point just before the
      target node.

3. **Two Pointer Traversal:**
    - **Front:** How are `left` and `right` pointers used to identify the node to remove?
    - **Back:** They move in tandem with a gap of `n` nodes; when `right` reaches the end, `left` is positioned just
      before the target node.

4. **Removing the Target Node:**
    - **Front:** How is the N-th node from the end removed in `removeNthFromEnd`?
    - **Back:** By adjusting `left.next` to skip the target node (`left.next = left.next.next`).

5. **Handling Edge Cases:**
    - **Front:** What edge cases does the `removeNthFromEnd` function handle?
    - **Back:** Removing the head node, lists with a single node, and lists where the node to remove is the last one.

6. **Function Flow:**
    - **Front:** Outline the key steps in the `removeNthFromEnd` function.
    - **Back:**
        1. Use a dummy node to handle edge cases.
        2. Advance the `right` pointer `n` steps ahead.
        3. Move both pointers until `right` reaches the end.
        4. Remove the target node by re-linking.
