# 🤖 Rule-Based Chatbot with Natural Language Processing

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://python.org)
[![NLTK](https://img.shields.io/badge/NLTK-3.9.1-green.svg)](https://www.nltk.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![UV](https://img.shields.io/badge/UV-Package%20Manager-orange.svg)](https://github.com/astral-sh/uv)

A sophisticated rule-based chatbot implementation using Python and NLTK that demonstrates fundamental Natural Language Processing concepts through pattern matching and response generation.

## 📋 Table of Contents

- [🎯 Project Overview](#-project-overview)
- [✨ Features](#-features)
- [🛠️ Technical Implementation](#️-technical-implementation)
- [🚀 Quick Start](#-quick-start)
- [📦 Installation Guide](#-installation-guide)
- [💻 Usage Examples](#-usage-examples)
- [🔧 Project Structure](#-project-structure)
- [📊 Pattern Matching System](#-pattern-matching-system)
- [🎨 Customization Guide](#-customization-guide)
- [🧪 Testing & Demo](#-testing--demo)
- [⚡ Performance & Limitations](#-performance--limitations)
- [🔮 Future Enhancements](#-future-enhancements)
- [📚 Learning Resources](#-learning-resources)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

## 🎯 Project Overview

This project implements a **rule-based chatbot** that serves as an educational demonstration of Natural Language Processing (NLP) fundamentals. The chatbot uses pattern matching with regular expressions to understand user input and generate contextually appropriate responses.

### 🎓 Educational Value

- **NLP Fundamentals**: Learn core concepts of text processing and pattern recognition
- **Regular Expressions**: Master regex patterns for text matching
- **Conversational AI**: Understand the basics of chatbot architecture
- **Python Programming**: Explore object-oriented design and modular programming

### 🏗️ Architecture

```
User Input → Pattern Matching → Response Selection → Natural Language Generation
```

## ✨ Features

### 🔍 Core Functionality
- **Advanced Pattern Matching**: Uses regex patterns for flexible input recognition
- **Natural Conversation Flow**: Implements pronoun reflection for human-like responses
- **Multi-Response System**: Each pattern supports multiple randomized responses
- **Context Extraction**: Captures and uses user-provided information (names, topics)
- **Graceful Fallbacks**: Handles unrecognized input professionally

### 🎛️ User Experience
- **Interactive Chat Interface**: Real-time conversation capability
- **Demo Mode**: Non-interactive showcase of all features
- **Easy Exit**: Simple conversation termination
- **Clear Feedback**: Informative responses and error handling

### 🔧 Technical Features
- **Modular Design**: Clean separation of concerns
- **Extensible Architecture**: Easy to add new patterns and responses
- **Dependency Management**: Modern Python package management with UV
- **Cross-Platform**: Works on Windows, macOS, and Linux

## 🛠️ Technical Implementation

### 🧠 Pattern Matching Engine

The chatbot uses NLTK's `Chat` class combined with regular expressions:

```python
class RuleBasedChatbot:
    def __init__(self, pairs):
        self.chat = Chat(pairs, reflections)
        
    def respond(self, user_input):
        return self.chat.respond(user_input)
```

### 🔄 Pronoun Reflection System

Automatic pronoun switching for natural conversations:

```python
reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}
```

### 📝 Response Generation

1. **Input Processing**: Normalize and clean user input
2. **Pattern Matching**: Find matching regex patterns
3. **Context Extraction**: Capture relevant information
4. **Response Selection**: Choose from available responses
5. **Natural Language Generation**: Apply pronoun reflection

## 🚀 Quick Start

### ⚡ One-Minute Setup

```bash
# Clone the repository
git clone https://github.com/karimmostafa-AI/Rule-Based-ChatBot.git
cd Rule-Based-ChatBot

# Install dependencies
uv sync

# Run the chatbot
uv run main.py
```

### 🎮 First Conversation

```
You: hello
Chatbot: Hi there! How may I assist you?

You: my name is Alice
Chatbot: Hello Alice! How can I assist you today?

You: tell me a joke
Chatbot: Why don't skeletons fight each other? They don't have the guts!

You: exit
Chatbot: Goodbye! Have a great day!
```

## 📦 Installation Guide

### 🔧 Prerequisites

- **Python 3.8+**: [Download Python](https://python.org/downloads/)
- **UV Package Manager**: Fast Python package manager

### 📥 Step-by-Step Installation

#### 1. Install UV Package Manager

**Windows (PowerShell):**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### 2. Clone the Repository

```bash
git clone https://github.com/karimmostafa-AI/Rule-Based-ChatBot.git
cd Rule-Based-ChatBot
```

#### 3. Set Up Virtual Environment

```bash
# Create virtual environment
uv venv

# Activate virtual environment
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

#### 4. Install Dependencies

```bash
# Install all dependencies
uv sync

# Or install manually
uv add nltk
```

#### 5. Verify Installation

```bash
# Run the demo to verify everything works
uv run demo.py
```

## 💻 Usage Examples

### 🎯 Interactive Mode

```bash
uv run main.py
```

**Sample Conversation:**
```
Hello, I am your chatbot! Type 'exit' to end the conversation.
You can ask me questions, tell me your name, or just chat!
--------------------------------------------------
You: hi there
Chatbot: Hello! How can I help you today?

You: what can you do?
Chatbot: I can chat with you, tell jokes, and help with basic questions!

You: can you help me with Python?
Chatbot: Sure! How can I assist you with Python?

You: thanks
Chatbot: You're welcome!
```

### 🎪 Demo Mode

```bash
uv run demo.py
```

**Output:**
```
Rule-Based Chatbot Demo
==================================================
You: hello
Chatbot: Hello! How can I help you today?
------------------------------
You: my name is John
Chatbot: Hello john! How can I assist you today?
------------------------------
...
```

### 🔧 Programmatic Usage

```python
from main import RuleBasedChatbot, pairs

# Initialize chatbot
bot = RuleBasedChatbot(pairs)

# Get response
response = bot.respond("Hello there!")
print(f"Bot: {response}")
```

## 🔧 Project Structure

```
rule-based-chatbot/
├── 📁 .venv/                    # Virtual environment
├── 📄 .gitignore               # Git ignore rules
├── 📄 .python-version          # Python version specification
├── 📄 main.py                  # 🎯 Main chatbot application
├── 📄 demo.py                  # 🎪 Demo script with examples
├── 📄 rule_based_chatbot.py    # 📚 Original implementation
├── 📄 pyproject.toml           # 📦 Project configuration
├── 📄 uv.lock                  # 🔒 Dependency lock file
└── 📄 README.md                # 📖 This comprehensive guide
```

### 📄 File Descriptions

| File | Purpose | Description |
|------|---------|-------------|
| `main.py` | Primary Application | Interactive chatbot with full conversation loop |
| `demo.py` | Demonstration | Non-interactive showcase of chatbot capabilities |
| `rule_based_chatbot.py` | Reference Implementation | Original standalone version |
| `pyproject.toml` | Project Configuration | Dependencies and project metadata |
| `uv.lock` | Dependency Lock | Ensures reproducible installations |

## 📊 Pattern Matching System

### 🎯 Pattern Categories

#### 1. **Greeting Patterns**
```python
[r"hi|hello|hey", ["Hello! How can I help you today?", "Hi there! How may I assist you?"]]
```

#### 2. **Identity Patterns**
```python
[r"my name is (.*)", ["Hello %1! How can I assist you today?"]]
[r"(.*) your name?", ["I am your friendly chatbot!"]]
```

#### 3. **Status Inquiry Patterns**
```python
[r"how are you?", ["I'm just a bot, but I'm doing well. How about you?"]]
```

#### 4. **Functional Patterns**
```python
[r"tell me a joke", ["Why don't skeletons fight each other? They don't have the guts!"]]
[r"what can you do?", ["I can chat with you, tell jokes, and help with basic questions!"]]
```

#### 5. **Help Patterns**
```python
[r"(.*) (help|assist) (.*)", ["Sure! How can I assist you with %3?"]]
```

#### 6. **Courtesy Patterns**
```python
[r"thank you|thanks", ["You're welcome!", "Happy to help!"]]
```

#### 7. **Exit Patterns**
```python
[r"bye|exit", ["Goodbye! Have a great day!", "See you later!"]]
```

#### 8. **Fallback Pattern**
```python
[r"(.*)", ["I'm sorry, I didn't understand that. Could you rephrase?", "Could you please elaborate?"]]
```

### 🔍 Pattern Matching Details

| Feature | Description | Example |
|---------|-------------|----------|
| **Literal Matching** | Exact word matching | `"hello"` matches "hello" |
| **Alternation** | Multiple options | `"hi\|hello\|hey"` matches any greeting |
| **Capture Groups** | Extract information | `"my name is (.*)"` captures the name |
| **Wildcards** | Match any text | `"(.*)"` matches any input |
| **Case Insensitive** | Ignore case differences | "HELLO" matches "hello" |

## 🎨 Customization Guide

### ➕ Adding New Patterns

1. **Define the Pattern**
```python
[r"what time is it", ["I don't have access to real-time information."]]
```

2. **Add Multiple Responses**
```python
[r"how's the weather", [
    "I don't have weather data, but I hope it's nice!",
    "I can't check the weather, but you could try a weather app!",
    "Sorry, I don't have access to weather information."
]]
```

3. **Use Capture Groups**
```python
[r"I like (.*)", [
    "That's great! %1 sounds interesting.",
    "Cool! I'd love to know more about %1."
]]
```

### 🎭 Advanced Patterns

#### Conditional Responses
```python
[r"(.*) (love|like|enjoy) (.*)", [
    "It's wonderful that you %2 %3!",
    "That's great! %3 must be really important to you."
]]
```

#### Question Detection
```python
[r"(.*) \?", [
    "That's an interesting question about %1.",
    "I'm not sure about %1, but it's worth exploring!"
]]
```

### 🎨 Response Personalization

```python
# Store user information
user_data = {}

# Enhanced pattern with memory
[r"my favorite (.*) is (.*)", [
    "Thanks for sharing! I'll remember that %1 is %2.",
    "Got it! %2 is your favorite %1."
]]
```

## 🧪 Testing & Demo

### 🎪 Running the Demo

```bash
# Run comprehensive demo
uv run demo.py

# Expected output shows all pattern categories
```

### 🧪 Testing Individual Patterns

```python
# Test specific patterns
test_cases = [
    ("hello", "greeting"),
    ("my name is Alice", "identity"),
    ("tell me a joke", "entertainment"),
    ("can you help me", "assistance"),
    ("random text", "fallback")
]

for input_text, category in test_cases:
    response = chatbot.respond(input_text)
    print(f"[{category}] {input_text} → {response}")
```

### 🔍 Pattern Debugging

```python
import re

# Test regex patterns
pattern = r"my name is (.*)"
test_input = "my name is John"
match = re.search(pattern, test_input, re.IGNORECASE)

if match:
    print(f"Captured: {match.group(1)}")
else:
    print("No match found")
```

## ⚡ Performance & Limitations

### 🚀 Performance Characteristics

- **Response Time**: ~10-50ms per query
- **Memory Usage**: ~10-20MB
- **Pattern Matching**: O(n) where n = number of patterns
- **Scalability**: Handles 100+ patterns efficiently

### ⚠️ Current Limitations

| Limitation | Impact | Mitigation |
|------------|--------|-----------|
| **No Learning** | Static responses | Use machine learning for adaptive responses |
| **No Context Memory** | Can't maintain conversation state | Implement conversation history |
| **Pattern Dependency** | Limited to predefined patterns | Add NLU models for intent recognition |
| **No Semantic Understanding** | Relies on exact matches | Integrate word embeddings or transformers |
| **Single Language** | English only | Add multilingual support |

### 🔧 Performance Optimization

```python
# Optimize pattern order (most common first)
pairs = [
    # High-frequency patterns first
    [r"hi|hello|hey", [...]],
    [r"(.*) help (.*)", [...]],
    # Less common patterns last
    [r"(.*)", [...]],  # Fallback pattern last
]
```

## 🔮 Future Enhancements

### 🎯 Immediate Improvements

1. **Enhanced Pattern Library**
   - Add 50+ new conversation patterns
   - Include domain-specific patterns (tech, health, etc.)
   - Implement pattern categories and tagging

2. **Conversation Memory**
   ```python
   class ConversationMemory:
       def __init__(self):
           self.history = []
           self.user_info = {}
   ```

3. **Response Quality**
   - Add response sentiment analysis
   - Implement response scoring system
   - Create response templates

### 🚀 Advanced Features

1. **Machine Learning Integration**
   ```python
   from transformers import pipeline
   
   intent_classifier = pipeline("text-classification", 
                               model="microsoft/DialoGPT-medium")
   ```

2. **Multi-Modal Support**
   - Image processing capabilities
   - Voice input/output
   - File upload handling

3. **External API Integration**
   ```python
   # Weather API integration
   import requests
   
   def get_weather(location):
       api_key = "your_api_key"
       response = requests.get(f"https://api.weather.com/{location}")
       return response.json()
   ```

4. **Web Interface**
   ```python
   from flask import Flask, render_template
   
   app = Flask(__name__)
   
   @app.route('/chat')
   def chat_interface():
       return render_template('chat.html')
   ```

### 🏗️ Architecture Evolution

```
Current: Rule-Based → Future: Hybrid AI

Rule-Based Engine + NLU + Context Manager + API Gateway
```

## 📚 Learning Resources

### 📖 Recommended Reading

1. **Natural Language Processing**
   - ["Natural Language Processing with Python"](https://www.nltk.org/book/) - NLTK Documentation
   - ["Speech and Language Processing"](https://web.stanford.edu/~jurafsky/slp3/) - Jurafsky & Martin

2. **Regular Expressions**
   - [RegexOne Interactive Tutorial](https://regexone.com/)
   - [Python re module documentation](https://docs.python.org/3/library/re.html)

3. **Conversational AI**
   - ["Building Chatbots with Python"](https://www.oreilly.com/library/view/building-chatbots-with/9781484268147/)
   - [Rasa Documentation](https://rasa.com/docs/)

### 🎓 Online Courses

- [Coursera NLP Specialization](https://www.coursera.org/specializations/natural-language-processing)
- [edX Introduction to Artificial Intelligence](https://www.edx.org/course/introduction-to-artificial-intelligence-ai)
- [Udacity Natural Language Processing Nanodegree](https://www.udacity.com/course/natural-language-processing-nanodegree--nd892)

### 🛠️ Tools & Libraries

- **NLTK**: Natural Language Toolkit
- **spaCy**: Industrial-strength NLP
- **Rasa**: Open-source conversational AI
- **ChatterBot**: Machine learning chatbot engine
- **Hugging Face Transformers**: State-of-the-art NLP models

## 🤝 Contributing

### 🎯 How to Contribute

1. **Fork the Repository**
   ```bash
   git clone https://github.com/karimmostafa-AI/Rule-Based-ChatBot.git
   cd Rule-Based-ChatBot
   ```

2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/new-patterns
   ```

3. **Make Your Changes**
   - Add new patterns to the `pairs` list
   - Update documentation
   - Add tests for new functionality

4. **Test Your Changes**
   ```bash
   uv run demo.py
   uv run main.py
   ```

5. **Submit a Pull Request**
   - Describe your changes
   - Include examples of new patterns
   - Reference any related issues

### 🎨 Contribution Ideas

- **New Pattern Categories**: Sports, cooking, travel, etc.
- **Language Support**: Add patterns for other languages
- **Response Improvements**: More natural and varied responses
- **Performance Optimizations**: Faster pattern matching
- **Documentation**: Improve examples and explanations
- **Testing**: Add unit tests and integration tests

### 📝 Code Style Guidelines

```python
# Follow PEP 8 style guide
# Use descriptive variable names
# Add docstrings to functions
# Include type hints where appropriate

def respond_to_user(user_input: str) -> str:
    """
    Generate a response to user input based on pattern matching.
    
    Args:
        user_input (str): The user's message
        
    Returns:
        str: The chatbot's response
    """
    return chatbot.respond(user_input)
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Karim Mostafa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

### 🙏 Acknowledgments

- **NLTK Team**: For providing excellent NLP tools and documentation
- **Astral Team**: For creating the fast and reliable UV package manager
- **Python Community**: For continuous support and excellent libraries
- **Open Source Contributors**: For inspiration and best practices

---

<div align="center">
  <strong>Built with ❤️ using Python, NLTK, and UV</strong>
  <br>
  <em>A comprehensive introduction to Natural Language Processing and Conversational AI</em>
</div>
