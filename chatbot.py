import tkinter as tk
from tkinter import scrolledtext
import cohere

# Initialize Cohere API client with your API key
# You can go to cohere and get your own api keys and replace this with your own
API_KEY = "Zni8otCGk21VClAAO391Jx9SJC77bEfVfyYFkLmx"
co = cohere.Client(API_KEY)

# Generate a response using Cohere
def get_response(prompt):
    try:
        response = co.generate(
            model='command',  # Use Cohere's "command" model
            prompt=prompt,
            max_tokens=50,
            temperature=0.7,
            k=50,  # Top-k sampling
            p=0.9,  # Nucleus sampling
            stop_sequences=["\n"]  # Stops at a newline for clean responses
        )
        return response.generations[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Send message to the chatbot
def send_message():
    user_input = user_entry.get()
    if user_input.strip():
        chat_display.insert(tk.END, f"You: {user_input}\n")
        response = get_response(user_input)
        chat_display.insert(tk.END, f"Jarvis Bot: {response}\n\n")
        user_entry.delete(0, tk.END)
    chat_display.yview(tk.END)

# GUI setup
root = tk.Tk()
root.title("3am chatbot ni Arron hehe")

chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, state='normal')
chat_display.pack(padx=10, pady=10)

user_entry = tk.Entry(root, width=50)
user_entry.pack(pady=5)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)

root.mainloop()

#created by: Arron Kian Parejas