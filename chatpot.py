import spacy

nlp = spacy.load("en_core_web_sm")


RESPONSES = {
    "greeting": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    "goodbye": ["Goodbye!", "See you later!", "Take care!"],
    "thanks": ["You're welcome!", "No problem!", "Anytime!"],
    "name": ["I'm a chatbot built with spaCy.", "You can call me ChatSpa!"],
    "help": ["I can answer simple questions. Try asking about my name or say hello."],
    "default": ["Sorry, I didn't understand that. Can you rephrase?"]
}


def get_intent(text):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc]

    if any(word in tokens for word in ["hello", "hi", "hey"]):
        return "greeting"
    elif any(word in tokens for word in ["bye", "goodbye", "see you"]):
        return "goodbye"
    elif any(word in tokens for word in ["thank", "thanks"]):
        return "thanks"
    elif any(word in tokens for word in ["name", "who are you"]):
        return "name"
    elif any(word in tokens for word in ["help", "can you do"]):
        return "help"
    else:
        return "default"


def get_response(intent):
    from random import choice
    return choice(RESPONSES[intent])

def chat():
    print("Chatbot is ready! (Type 'exit' to quit)\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Bot:", get_response("goodbye"))
            break

        intent = get_intent(user_input)
        response = get_response(intent)
        print("Bot:", response)

if __name__ == "__main__":
    chat()
