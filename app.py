

from flask import Flask, render_template, send_from_directory
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('script.js')
def script():
    return send_from_directory('.', 'script.js')

@socketio.on('user_message')
def handle_user_message(message):
    response = generate_bot_response(message)
    emit('bot_response', response)

def generate_bot_response(msg):
    msg = msg.lower()

    if "hello" in msg or "hi" in msg:
        return "Hey there! 👋 How can I help you today?"
    elif "how are you" in msg:
        return "I'm doing great, thanks for asking! Hope you're doing well too 😊"
    elif "what's your name" in msg or "who are you" in msg:
        return "I'm your friendly real-time chatbot 🤖"
    elif "bye" in msg or "goodbye" in msg:
        return "Take care! Hope to chat with you again soon 👋"
    elif "thank you" in msg or "thanks" in msg:
        return "You're most welcome! 🙏"
    elif "joke" in msg:
        return "Why don't scientists trust atoms? Because they make up everything! 😄"
    elif "weather" in msg:
        return "I can't predict the weather yet, but it's always sunny in this chat! ☀"
    elif "help" in msg:
        return "Sure! You can ask me anything — from jokes to basic questions!"
    elif "your creator" in msg:
        return "I was created by an awesome developer 😎"
    else:
        return "Hmm... I'm not sure about that 🤔. Try asking something else!"

if __name__ == '__main__':
    socketio.run(app, debug=True)