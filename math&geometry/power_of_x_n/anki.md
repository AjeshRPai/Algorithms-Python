## Anki card based on key points:

**Front**:
What are the key points of the efficient myPow (x^n) implementation?

**Back**:
1. Use binary exponentiation (O(log n) time)
2. Handle base cases: x^0 = 1, 0^n = 0
3. For negative n: use 1/x, make n positive
4. While loop: n > 0
5. If n odd: result *= x
6. Each iteration: x *= x, n //= 2
7. Breaks exponent into powers of 2