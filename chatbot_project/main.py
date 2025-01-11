import random
import re
from responses import get_response
from training_data import intents
import sympy as sp
import math
def extract_simple_math_operation(user_input):
    """
    Extracts and solves simple arithmetic operations from the user's input.
    """
    
    # Patterns for matching arithmetic operations
    patterns = [
        r"(-?\d+)\s*(plus|[\+\-])\s*(-?\d+)",            # Handles addition and alternative symbols (+, -)
        r"(-?\d+)\s*(minus|[\-\–])\s*(-?\d+)",           # Handles subtraction (including long dash)
        r"(-?\d+)\s*(times|\*)\s*(-?\d+)",               # Handles multiplication
        r"(-?\d+)\s*(divided by|\/)\s*(-?\d+)",          # Handles division
        r"(-?\d+)\s*\+\s*(-?\d+)",                       # Handles alternative addition with +
        r"(-?\d+)\s*\-\s*(-?\d+)",                       # Handles alternative subtraction with -
        r"(-?\d+)\s*\*\s*(-?\d+)",                       # Handles alternative multiplication with *
        r"(-?\d+)\s*\/\s*(-?\d+)"                        # Handles alternative division with /
    ]
    user_input = user_input.lower()  # Convert input to lowercase for case insensitivity
    
    for pattern in patterns:
        match = re.search(pattern, user_input)  # Use re.search to allow matching anywhere in the input
        if match:
            num1 = float(match.group(1))
            num2 = float(match.group(2))
            return num1, num2, pattern
    
    return None, None, None  # If no match is found
def extract_advanced_math(user_input):
    """
    Extract and solve advanced math operations like integration, derivatives, algebra, etc.
    """
    # Handle integration or integral
    if "integrate" in user_input.lower() or "integral" in user_input.lower():
        return 'integration', user_input
    
    # Handle differentiation or derivative
    elif "differentiate" in user_input.lower() or "derivative" in user_input.lower():
        return 'derivative', user_input
    
    # Handle simplifying expressions
    elif "simplify" in user_input.lower():
        return 'simplify', user_input
    
    # Handle solving equations
    elif "solve equation" in user_input.lower() or "solve" in user_input.lower():
        return 'solve_equation', user_input
    
    # Handle matrix operations
    elif "matrix" in user_input.lower():
        return 'matrix', user_input
    
    # Handle determinant calculation
    elif "determinant" in user_input.lower():
        return 'determinant', user_input
    
    # Handle eigenvalues
    elif "eigenvalue" in user_input.lower() or "eigenvalues" in user_input.lower():
        return 'eigenvalue', user_input
    
    # Handle factorization
    elif "factor" in user_input.lower():
        return 'factor', user_input
    
    # Handle logarithms
    elif "log" in user_input.lower():
        return 'logarithm', user_input
    
    # Handle trigonometric operations (sin, cos, tan)
    elif "sin" in user_input.lower() or "cos" in user_input.lower() or "tan" in user_input.lower():
        return 'trigonometry', user_input
    
    # Handle solving systems of equations
    elif "system of equations" in user_input.lower() or "simultaneous equations" in user_input.lower():
        return 'system_of_equations', user_input
    
    # Handle quadratic equations
    elif "quadratic equation" in user_input.lower():
        return 'quadratic_equation', user_input
    
    # Handle finding roots of an equation
    elif "roots of" in user_input.lower():
        return 'roots', user_input
    
    # Handle finding limits
    elif "limit" in user_input.lower():
        return 'limit', user_input
    
    # Handle summation (Σ notation)
    elif "summation" in user_input.lower() or "sum" in user_input.lower():
        return 'summation', user_input
    
    # Handle series (arithmetic or geometric series)
    elif "series" in user_input.lower():
        return 'series', user_input
    
    # Handle prime factorization
    elif "prime factorization" in user_input.lower():
        return 'prime_factorization', user_input
    
    # Handle absolute value
    elif "absolute value" in user_input.lower() or "modulus" in user_input.lower():
        return 'absolute_value', user_input
    
    # Handle solving for derivatives of parametric equations
    elif "parametric derivative" in user_input.lower():
        return 'parametric_derivative', user_input
    
    # Handle finding matrix inverse
    elif "matrix inverse" in user_input.lower():
        return 'matrix_inverse', user_input
    
    # Default case: Return None if no advanced operation matched
    else:
        return None, None
def chatbot_response(user_input):
    """
    This function receives user input, matches it to training patterns,
    and returns an appropriate response.
    """
    # Check for simple math operations
    num1, num2, pattern = extract_simple_math_operation(user_input)
    if num1 is not None and num2 is not None:
        # Perform the corresponding operation based on the pattern
        if "plus" in pattern or "+" in pattern:
            result = num1 + num2
        elif "minus" in pattern or "-" in pattern:
            result = num1 - num2
        elif "times" in pattern or "*" in pattern:
            result = num1 * num2  # Fixed multiplication
        elif "divided by" in pattern or "/" in pattern:
            if num2 != 0:
                result = num1 / num2  # Fixed division
            else:
                return "Cannot divide by zero."
        
        return f"The result is {result}."
    else:
        return "Sorry, I couldn't understand that operation."
    # Advanced math operations (left unchanged)
    operation, expression = extract_advanced_math(user_input)
    
    if operation == 'integration':
        try:
            expr = sp.sympify(expression.split("integrate")[-1])
            integral = sp.integrate(expr)
            return f"The integral of {expr} is {integral}."
        except Exception as e:
            return f"Error in integration: {e}"

    elif operation == 'derivative':
        try:
            expr = sp.sympify(expression.split("differentiate")[-1])
            derivative = sp.diff(expr)
            return f"The derivative of {expr} is {derivative}."
        except Exception as e:
            return f"Error in differentiation: {e}"

    elif operation == 'simplify':
        try:
            expr = sp.sympify(expression.split("simplify")[-1])
            simplified = sp.simplify(expr)
            return f"The simplified expression is {simplified}."
        except Exception as e:
            return f"Error in simplifying the expression: {e}"

    elif operation == 'solve_equation':
        try:
            expr = sp.sympify(expression.split("solve equation")[-1])
            solution = sp.solve(expr)
            return f"The solution to the equation {expr} is {solution}."
        except Exception as e:
            return f"Error in solving the equation: {e}"

    elif operation == 'matrix':
        try:
            expr = sp.Matrix(sp.sympify(expression.split("matrix")[-1]))
            return f"The matrix is: {expr}"
        except Exception as e:
            return f"Error in matrix operation: {e}"

    elif operation == 'determinant':
        try:
            expr = sp.Matrix(sp.sympify(expression.split("determinant")[-1]))
            det = expr.det()
            return f"The determinant of the matrix is {det}."
        except Exception as e:
            return f"Error in calculating the determinant: {e}"

    elif operation == 'eigenvalue':
        try:
            expr = sp.Matrix(sp.sympify(expression.split("eigenvalue")[-1]))
            eigenvals = expr.eigenvals()
            return f"The eigenvalues of the matrix are {eigenvals}."
        except Exception as e:
            return f"Error in finding eigenvalues: {e}"

    elif operation == 'factor':
        try:
            expr = sp.sympify(expression.split("factor")[-1])
            factored = sp.factor(expr)
            return f"The factored form of {expr} is {factored}."
        except Exception as e:
            return f"Error in factoring the expression: {e}"

    elif operation == 'logarithm':
        try:
            base_match = re.search(r"log\((.*?)\)", expression)
            if base_match:
                number = float(base_match.group(1))
                result = math.log(number)
                return f"The logarithm of {number} is {result}."
            else:
                return "Please specify the number for the logarithm."
        except Exception as e:
            return f"Error in logarithmic calculation: {e}"

    elif operation == 'trigonometry':
        try:
            if "sin" in user_input.lower():
                angle = float(re.search(r"sin\((.*?)\)", user_input).group(1))
                result = math.sin(math.radians(angle))
                return f"The sine of {angle} degrees is {result}."
            elif "cos" in user_input.lower():
                angle = float(re.search(r"cos\((.*?)\)", user_input).group(1))
                result = math.cos(math.radians(angle))
                return f"The cosine of {angle} degrees is {result}."
            elif "tan" in user_input.lower():
                angle = float(re.search(r"tan\((.*?)\)", user_input).group(1))
                result = math.tan(math.radians(angle))
                return f"The tangent of {angle} degrees is {result}."
        except Exception as e:
            return f"Error in trigonometric calculation: {e}"

    # Check for greetings or other intents using get_response function
    for intent in intents:
        for pattern in intent["patterns"]:
            if re.search(pattern.lower(), user_input.lower()):
                return get_response(intent["intent"])  # Use get_response function
    
    return "Sorry, I didn't understand that."

def main():
    """
    Main loop for the chatbot to interact with the user.
    """
    print("Chatbot is running. Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "quit":
            print("Chatbot is shutting down...")
            break
        
        # Get and display chatbot's response
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
if __name__ == "__main__":
    main()
