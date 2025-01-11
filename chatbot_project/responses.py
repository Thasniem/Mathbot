import random

def get_response(intent):
    """
    This function generates a random response based on the intent.
    """
    responses_dict = {
        "greeting": [
            "Hello! How can I assist you today?",
            "Hi there! What can I do for you?",
            "Hey! How's it going?"
        ],
        "goodbye": [
            "Goodbye! Have a great day!",
            "See you later, take care!",
            "Bye! Come back if you need anything!"
        ],
        "thanks": [
            "You're welcome!",
            "Glad to be of help!",
            "Anytime!"
        ],
        "jokes": [
            "Why don't skeletons fight each other? They don't have the guts!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "Why don’t programmers like nature? It has too many bugs."
        ],
        "help": [
            "I can help you with basic math problems, integrals, derivatives, solving equations, and more.",
            "Ask me anything! Whether it's about math or fun facts, I am here to assist!",
            "I can assist you with various types of calculations and information."
        ]
    }

    # Choose a random response for the matched intent
    if intent in responses_dict:
        return random.choice(responses_dict[intent])
    else:
        return "Sorry, I didn't understand that."
