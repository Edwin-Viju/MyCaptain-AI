def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    a, b = 0, 1
    sequence = [a, b]

    while len(sequence) < n:
        number = a + b
        a = b
        b = number
        sequence.append(number)

    return sequence

terms = int(input("Enter the number of Fibonacci terms: "))
fib = fibonacci(terms)
print("The Fibonacci sequence with", num_terms, "terms is:", fib)
