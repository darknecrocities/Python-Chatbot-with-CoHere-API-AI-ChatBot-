import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk
import cohere
import random
import time
from PIL import Image, ImageTk

# Initialize Cohere API client (Replace with your actual API key)
API_KEY = "Zni8otCGk21VClAAO391Jx9SJC77bEfVfyYFkLmx"
co = cohere.Client(API_KEY)

# Fun facts & jokes
fun_responses = [
    "Did you know? The first computer was invented in the 1940s!",
    "Here's a joke: Why don’t programmers like nature? It has too many bugs!",
    "Fun fact: Python was named after Monty Python, not the snake!",
    "I'm here to chat, tell jokes, and be your AI buddy! How’s your day?"
]

# Store chat history for context
chat_history = []
user_messages = []  # Store user input for history navigation
history_index = -1  # Track user message navigation

# Background images
background_images = ["1.webp", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
current_bg_index = 0


def get_response(prompt):
    """Generate chatbot response using Cohere or fun responses."""
    global chat_history
    chat_history.append(f"You: {prompt}")

    if any(word in prompt.lower() for word in ["joke", "fun fact", "bored"]):
        return random.choice(fun_responses)

    try:
        context = "\n".join(chat_history[-3:])  # Keep last 3 exchanges for better context
        full_prompt = f"Conversation so far:\n{context}\nBot: (respond in detail)"

        response = co.generate(
            model='command',
            prompt=full_prompt,
            max_tokens=1500,
            temperature=0.7,
            k=100,
            p=0.95
        )

        reply = response.generations[0].text.strip()
        chat_history.append(f"Loopy Bot: {reply}")
        return reply
    except Exception as e:
        return f"Error: {str(e)}"


def typing_effect(widget, text):
    """Simulate typing effect for bot messages with color."""
    widget.insert(tk.END, "Loopy Bot: ", "bot")
    for char in text:
        widget.insert(tk.END, char, "bot")
        widget.update()
        time.sleep(0.02)
    widget.insert(tk.END, "\n\n")
    widget.yview(tk.END)


def send_message(event=None):
    """Send message to the chatbot and get a response."""
    global history_index

    user_input = user_entry.get().strip()
    if user_input:
        chat_display.insert(tk.END, f"You: {user_input}\n", "user")  # User message (blue)
        user_messages.append(user_input)  # Store user input
        history_index = len(user_messages)  # Reset history index

        user_entry.delete(0, tk.END)
        root.update()

        response = get_response(user_input)
        typing_effect(chat_display, response)

    if user_input.lower() == "exit":
        root.quit()


def clear_chat():
    """Clear chat history."""
    chat_display.delete(1.0, tk.END)
    chat_display.insert(tk.END, "Loopy Bot: Hi! I'm Loopy, your fun chatbot! Type 'exit' to quit.\n\n", "bot")


def change_theme():
    """Change background image dynamically."""
    global current_bg_index
    current_bg_index = (current_bg_index + 1) % len(background_images)

    new_bg = Image.open(background_images[current_bg_index])
    new_bg = new_bg.resize((500, 500), Image.LANCZOS)
    new_bg = ImageTk.PhotoImage(new_bg)

    background_label.config(image=new_bg)
    background_label.image = new_bg  # Keep reference to prevent garbage collection


def navigate_history(event):
    """Navigate through user message history using Up/Down arrows."""
    global history_index
    if user_messages:
        if event.keysym == "Up" and history_index > 0:
            history_index -= 1
        elif event.keysym == "Down" and history_index < len(user_messages) - 1:
            history_index += 1
        elif event.keysym == "Down":
            history_index = len(user_messages)  # Reset if moving beyond last

        user_entry.delete(0, tk.END)
        if history_index < len(user_messages):
            user_entry.insert(0, user_messages[history_index])


# GUI Setup
root = tk.Tk()
root.title("LOOPY CHATBOT")
root.geometry("500x500")
root.resizable(False, False)

# Background Label
background_label = tk.Label(root)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
change_theme()  # Set initial background

# Chat Window
chat_label = tk.Label(root, text="Chat Window", font=("Arial", 12, "bold"), bg="#D1C4E9")
chat_label.pack()

chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, state='normal', bg="white", fg="black")
chat_display.pack(padx=10, pady=10)

# Define text color styles
chat_display.tag_config("user", foreground="blue", font=("Arial", 10, "bold"))  # User messages in blue
chat_display.tag_config("bot", foreground="purple", font=("Arial", 10, "bold"))  # Bot messages in purple

# Initial Greeting
chat_display.insert(tk.END, "Loopy Bot: Hi! I'm Loopy, your fun chatbot! Type 'exit' to quit.\n\n", "bot")

# User Input Box
user_entry = tk.Entry(root, width=50)
user_entry.pack(pady=5)
user_entry.bind("<Return>", send_message)
user_entry.bind("<Up>", navigate_history)
user_entry.bind("<Down>", navigate_history)

# Buttons
send_button = tk.Button(root, text="Send", command=send_message, bg="#673AB7", fg="white")
send_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear Chat", command=clear_chat, bg="#FF5722", fg="white")
clear_button.pack(pady=5)

theme_button = tk.Button(root, text="Change Theme", command=change_theme, bg="#009688", fg="white")
theme_button.pack(pady=5)

# Start GUI
root.mainloop()
