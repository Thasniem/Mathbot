intents = [
    {
        "intent": "greeting",
        "patterns": [
            "Hi",
            "Hello",
            "Good morning",
            "Hey",
            "How are you?"
        ],
        "responses": [
            "Hello! How can I assist you today?",
            "Hi there! What can I do for you?",
            "Hey! How's it going?"
        ]
    },
    {
        "intent": "goodbye",
        "patterns": [
            "Bye",
            "Goodbye",
            "See you later",
            "Take care"
        ],
        "responses": [
            "Goodbye! Have a great day!",
            "See you later, take care!",
            "Bye! Come back if you need anything!"
        ]
    },
    {
        "intent": "thanks",
        "patterns": [
            "Thanks",
            "Thank you",
            "Thanks a lot",
            "Thank you so much"
        ],
        "responses": [
            "You're welcome!",
            "Glad to be of help!",
            "Anytime!"
        ]
    },
    {
        "intent": "math_simple",
        "patterns": [
            "What is {num1} plus {num2}?",
            "What is {num1} minus {num2}?",
            "What is {num1} times {num2}?",
            "What is {num1} divided by {num2}?",
            "Solve {num1} + {num2}",
            "Solve {num1} - {num2}",
            "Solve {num1} * {num2}",
            "Solve {num1} / {num2}"
        ],
        "responses": [
            "Let's solve that: {result}"
        ]
    },
    {
        "intent": "math_integration",
        "patterns": [
            "Integrate {expression}",
            "Find the integral of {expression}",
            "Solve the integral of {expression}",
            "What is the integral of {expression}?"
        ],
        "responses": [
            "The integral of {expression} is {result}."
        ]
    },
    {
        "intent": "math_derivative",
        "patterns": [
            "Differentiate {expression}",
            "Find the derivative of {expression}",
            "Solve the derivative of {expression}",
            "What is the derivative of {expression}?"
        ],
        "responses": [
            "The derivative of {expression} is {result}."
        ]
    },
    {
        "intent": "math_simplify",
        "patterns": [
            "Simplify {expression}",
            "Simplify this: {expression}",
            "Reduce {expression}",
            "Solve {expression}"
        ],
        "responses": [
            "The simplified form of {expression} is {result}."
        ]
    },
    {
        "intent": "math_solve_equation",
        "patterns": [
            "Solve the equation {equation}",
            "Find the solution for {equation}",
            "What is the solution for {equation}?"
        ],
        "responses": [
            "The solution to {equation} is {result}."
        ]
    },
    {
        "intent": "math_matrix",
        "patterns": [
            "What is the matrix {expression}?",
            "Solve the matrix {expression}",
            "Find the matrix {expression}"
        ],
        "responses": [
            "The matrix is {result}."
        ]
    },
    {
        "intent": "math_determinant",
        "patterns": [
            "What is the determinant of {matrix}?",
            "Find the determinant of {matrix}",
            "Solve the determinant of {matrix}"
        ],
        "responses": [
            "The determinant of the matrix is {result}."
        ]
    },
    {
        "intent": "math_eigenvalue",
        "patterns": [
            "What are the eigenvalues of {matrix}?",
            "Find the eigenvalues of {matrix}",
            "Solve for eigenvalues of {matrix}"
        ],
        "responses": [
            "The eigenvalues of the matrix are {result}."
        ]
    },
    {
        "intent": "math_factor",
        "patterns": [
            "Factor {expression}",
            "Factor this expression: {expression}",
            "Solve {expression} by factoring"
        ],
        "responses": [
            "The factored form of {expression} is {result}."
        ]
    }
]
