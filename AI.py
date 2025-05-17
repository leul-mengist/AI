import re
import math

# Math-focused responses (expanded to 100 entries)
responses = {
    "hello": "Hi there! Ready to talk about math?",
    "hi": "Hey! Math is fun, let's dive in!",
    "how are you": "I'm great! Math keeps me energized!",
    "bye": "Goodbye! Keep calculating!",
    "what is 2 + 2": "2 + 2 equals 4!",
    "what is 10 - 4": "10 - 4 equals 6!",
    "what is 3 * 7": "3 times 7 equals 21!",
    "what is 24 / 8": "24 divided by 8 equals 3!",
    "what is the square root of 16": "The square root of 16 is 4!",
    "what is 5 squared": "5 squared is 25!",
    "what is the cube of 3": "3 cubed is 27!",
    "what is the power of 2^10": "2 to the power of 10 is 1024!",
    "what is pi": "Pi is approximately 3.14159!",
    "what is the area of a circle": "The area of a circle is A = πr²!",
    "what is the perimeter of a square": "The perimeter of a square is 4 times its side length!",
    "what is the volume of a cube": "The volume of a cube is V = s³!",
    "what is an equation": "An equation is a statement that shows two expressions are equal!",
    "what is an inequality": "An inequality shows that one expression is greater or smaller than another!",
    "what is a prime number": "A prime number is a number greater than 1 that has only two divisors: 1 and itself!",
    "is 7 prime": "Yes! 7 is a prime number because it has no divisors other than 1 and 7!",
    "is 8 prime": "No, 8 is not a prime number because it can be divided by 2 and 4!",
    "what is factorial 5": "5! (5 factorial) is 5 × 4 × 3 × 2 × 1 = 120!",
    "what is 0 factorial": "0! is defined as 1!",
    "what is an angle": "An angle is the space between two intersecting lines measured in degrees!",
    "what is a right angle": "A right angle is exactly 90 degrees!",
    "what is a straight angle": "A straight angle is exactly 180 degrees!",
    "what is a triangle": "A triangle is a polygon with three sides!",
    "what is the Pythagorean theorem": "The Pythagorean theorem states a² + b² = c² for right triangles!",
    "what is an integral": "An integral calculates the area under a curve!",
    "what is a derivative": "A derivative measures the rate of change of a function!",
    "differentiate x^2": "The derivative of x² is 2x!",
    "integrate x^2": "The integral of x² is (1/3)x³ + C!",
    "what is Euler’s number": "Euler's number e is approximately 2.718!",
    "what is a logarithm": "A logarithm is the inverse of exponentiation!",
    "solve x + 5 = 10": "Subtract 5 from both sides: x = 5!",
    "solve 2x = 8": "Divide by 2: x = 4!",
    "what is the Fibonacci sequence": "The Fibonacci sequence starts with 0 and 1, and each term is the sum of the two previous terms!",
    "convert 1/4 to decimal": "1/4 in decimal form is 0.25!",
    "convert 0.75 to fraction": "0.75 as a fraction is 3/4!",
    "what is probability": "Probability measures how likely an event is to happen!",
    "what is a histogram": "A histogram shows data distribution using bars!",
    "what is a parabola": "A parabola is the graph of a quadratic function!",
    "what is math":"Maths, or mathematics, is the study of numbers, shapes, patterns, and logical relationships!",
}


def solve_math(input_text):
    input_text = input_text.lower()

    # Basic math operations (addition, subtraction, multiplication, division)
    match = re.match(r"what is (\d+) ([+\-*/]) (\d+)", input_text)
    if match:
        num1, operator, num2 = int(match.group(1)), match.group(2), int(match.group(3))
        if operator == '+':
            return f"{num1} + {num2} = {num1 + num2}"
        elif operator == '-':
            return f"{num1} - {num2} = {num1 - num2}"
        elif operator == '*':
            return f"{num1} × {num2} = {num1 * num2}"
        elif operator == '/':
            return f"{num1} ÷ {num2} = {num1 / num2:.2f}" if num2 != 0 else "Division by zero is undefined!"

    # Exponents and square roots
    match = re.match(r"what is (\d+) (\^|\*\*) (\d+)", input_text)
    if match:
        base, power = int(match.group(1)), int(match.group(3))
        return f"{base} to the power of {power} is {base ** power}"

    match = re.match(r"what is the square root of (\d+)", input_text)
    if match:
        num = int(match.group(1))
        return f"The square root of {num} is {num ** 0.5:.2f}"

    # Factorials
    match = re.match(r"what is factorial (\d+)", input_text)
    if match:
        num = int(match.group(1))
        factorial = math.factorial(num)
        return f"{num}! (factorial) is {factorial}"

    # Logarithms
    match = re.match(r"what is log base (\d+) of (\d+)", input_text)
    if match:
        base, num = int(match.group(1)), int(match.group(2))
        return f"log base {base} of {num} is {math.log(num, base):.4f}"

    # Standard responses
    if input_text in responses:
        return responses[input_text]
    else:
        print("AI: I don’t know that yet. Teach me!")
        new_response = input("You: ")
        responses[input_text] = new_response
        print("AI: Got it! I’ll remember that next time.")
        return new_response

# Example usage
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("AI: Bye!")
        break
    print("AI:", solve_math(user_input))


    
# Example usage
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("AI: Bye!")
        break
    print("AI:",(user_input))