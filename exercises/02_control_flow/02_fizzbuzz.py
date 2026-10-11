"""FizzBuzz sequence

Concepts: for, range, if/elif/else, lists
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Return strings for integers 1 through n inclusive: Fizz for multiples of 3,
Buzz for multiples of 5, FizzBuzz for both, otherwise the number. n <= 0 -> [].

HINT
Check the combined condition first.

STRETCH
Accept a mapping of divisors to words.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

def fizzbuzz(n):
    result = []
    for number in range(1, n + 1):
        if number % 15 == 0:
            result.append('FizzBuzz')
        elif number % 3 == 0:
            result.append('Fizz')
        elif number % 5 == 0:
            result.append('Buzz')
        else:
            result.append(str(number))
    return result


def check():
    assert fizzbuzz(5) == ['1', '2', 'Fizz', '4', 'Buzz']
    assert fizzbuzz(15)[-1] == 'FizzBuzz'
    assert fizzbuzz(0) == []


if __name__ == "__main__":
    check()
    print("PASS: FizzBuzz sequence")
