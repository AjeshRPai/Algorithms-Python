## Key points to memorize this solution:

1. Use the binary exponentiation algorithm for efficiency (O(log n) time complexity).
2. Handle base cases: x^0 = 1, 0^n = 0 (for n != 0).
3. For negative exponents, use the reciprocal of x and make n positive.
4. Use a while loop to iterate while n > 0.
5. If n is odd, multiply the result by x.
6. In each iteration, square x and halve n.
7. The algorithm works by breaking down the exponent into powers of 2.



