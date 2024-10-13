import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?", "Hi %1! What can I do for you?"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created to assist you!", "You can call me ChatBot."]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you!", "I'm just a bunch of code, but thanks for asking!"]
    ],
    [
        r"quit",
        ["Goodbye! Have a great day!", "See you later!"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't understand. Can you rephrase that?"]
    ],
]

def chatbot():
    print("Hi! I'm a ChatBot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
