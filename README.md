Chatbot Application Setup Guide
This project is a simple chatbot application that utilizes the Cohere API for natural language processing and Tkinter for the graphical user interface. The following steps will guide you through setting up the necessary libraries, obtaining your API key, and running the application.

✨ Prerequisites
Before running the script, ensure that you have the necessary software and libraries installed.

1. Install Required Packages
The application depends on the following Python libraries:

Cohere Python SDK: Used to interact with the Cohere API for natural language processing.
Tkinter: A built-in library in Python for creating graphical user interfaces.
Cohere Python SDK
To install the Cohere SDK, run the following command in your terminal or command prompt:

bash
Copy code
pip install cohere
Tkinter (For GUI)
Windows/Mac:
Tkinter is typically bundled with Python, so no installation should be required. If you're using a minimal Python installation, you may need to install it.

Linux (Ubuntu/Debian-based Systems):
To install Tkinter on Linux, run the following command in the terminal:

bash
Copy code
sudo apt-get install python3-tk
Upgrade Pip (Optional but Recommended)
Ensure you have the latest version of pip by upgrading it. This will help avoid potential compatibility issues with libraries:

bash
Copy code
pip install --upgrade pip
🔑 Set Up Your Cohere API Key
To use the Cohere API, you will need an API key.

Create an account at Cohere.
Generate an API key from your Cohere dashboard.
Once you have your API key, replace the API_KEY placeholder in the code with your actual key:

python
Copy code
API_KEY = "your-cohere-api-key-here"
🚀 Running the Application
Now that you've installed the necessary libraries and set your API key, you can run the application!

Open your terminal or command prompt.
Navigate to the directory where your script is located.
Run the script using the following command:
bash
Copy code
python your_script_name.py
This will launch the Tkinter GUI for your chatbot. You can now start interacting with the bot.

📜 Example Usage
Step 1: Install dependencies (see above).
Step 2: Set your API key in the code.
Step 3: Run the script and interact with the chatbot.
📝 Credits
This project was developed by Arron Parejas. Special thanks to the amazing developers at Cohere for providing the API that powers the natural language processing capabilities of this chatbot.

⚡ Support
If you encounter any issues, feel free to reach out by creating an issue in this repository or contact me directly at [parejasarronkian@gmail.com].
