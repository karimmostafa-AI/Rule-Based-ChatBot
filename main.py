import nltk
import re
from nltk.chat.util import Chat, reflections

# Download required NLTK datasets
try:
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    print("NLTK datasets downloaded successfully!")
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

def chat_with_bot():
    print("Hello, I am your chatbot! Type 'exit' to end the conversation.")
    print("You can ask me questions, tell me your name, or just chat!")
    print("-" * 50)
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a nice day!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

def main():
    global chatbot
    chatbot = RuleBasedChatbot(pairs)
    chat_with_bot()

if __name__ == "__main__":
    main()
