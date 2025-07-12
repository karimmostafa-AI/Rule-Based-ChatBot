import nltk
import re
from nltk.chat.util import Chat, reflections

# Download required NLTK datasets
try:
    nltk.download('punkt', quiet=True)
    nltk.download('averaged_perceptron_tagger', quiet=True)
    print("NLTK datasets ready!")
except Exception as e:
    print(f"Error downloading NLTK datasets: {e}")

# Define patterns and responses
pairs = [
    [r"hi|hello|hey", ["Hello! How can I help you today?", "Hi there! How may I assist you?"]],
    [r"my name is (.*)", ["Hello %1! How can I assist you today?"]],
    [r"(.*) your name?", ["I am your friendly chatbot!"]],
    [r"how are you?", ["I'm just a bot, but I'm doing well. How about you?"]],
    [r"tell me a joke", ["Why don't skeletons fight each other? They don't have the guts!"]],
    [r"(.*) (help|assist) (.*)", ["Sure! How can I assist you with %3?"]],
    [r"bye|exit", ["Goodbye! Have a great day!", "See you later!"]],
    [r"what can you do?", ["I can chat with you, tell jokes, and help with basic questions!"]],
    [r"(.*) weather (.*)", ["I'm sorry, I don't have access to weather information."]],
    [r"(.*) time (.*)", ["I don't have access to real-time information."]],
    [r"thank you|thanks", ["You're welcome!", "Happy to help!"]],
    [r"(.*)", ["I'm sorry, I didn't understand that. Could you rephrase?", "Could you please elaborate?"]]
]

class RuleBasedChatbot:
    def __init__(self, pairs):
        self.chat = Chat(pairs, reflections)
        
    def respond(self, user_input):
        return self.chat.respond(user_input)

def demo_chatbot():
    print("Rule-Based Chatbot Demo")
    print("=" * 50)
    
    chatbot = RuleBasedChatbot(pairs)
    
    # Demo conversations
    test_inputs = [
        "hello",
        "my name is John",
        "what's your name?",
        "how are you?",
        "tell me a joke",
        "can you help me with coding?",
        "what can you do?",
        "thanks",
        "some random input that doesn't match patterns"
    ]
    
    for user_input in test_inputs:
        response = chatbot.respond(user_input)
        print(f"You: {user_input}")
        print(f"Chatbot: {response}")
        print("-" * 30)
    
    print("\nDemo completed! The chatbot successfully matches patterns and responds appropriately.")

if __name__ == "__main__":
    demo_chatbot()
