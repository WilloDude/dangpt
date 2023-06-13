import tkinter as tk
from transformers import GPTNeoForCausalLM, GPT2Tokenizer
import threading
import time

# Load the GPT-Neo model and tokenizer
model = GPTNeoForCausalLM.from_pretrained('EleutherAI/gpt-neo-1.3B')
tokenizer = GPT2Tokenizer.from_pretrained('EleutherAI/gpt-neo-1.3B')

# Set the padding token for the tokenizer
tokenizer.pad_token = tokenizer.eos_token

# Create the GUI window
window = tk.Tk()
window.title("Neo-GPT Chatbot")
window.configure(bg="#202020")  # Set the background color

# Create the chat log
chat_log = tk.Text(window, height=20, width=50, fg="#FFFFFF", bg="#202020", insertbackground="#FFFFFF")
chat_log.tag_configure("bot", foreground="#FF4081")
chat_log.pack()

# Create the input text box
input_text = tk.Text(window, height=4, width=50, fg="#FFFFFF", bg="#363636", insertbackground="#FFFFFF")
input_text.pack()

# Create the "Send" button
send_button = tk.Button(window, text="Send", command=generate_response, fg="#FFFFFF", bg="#363636", activebackground="#363636")
send_button.pack()

# Function to handle user input and generate model response
def generate_response():
    user_input = input_text.get("1.0", tk.END).strip()
    input_ids = tokenizer.encode(user_input, return_tensors='pt')

    # Generate a response from the model
    output = model.generate(input_ids, max_length=100, num_return_sequences=1, temperature=0.7)

    # Decode the generated output
    response = tokenizer.decode(output[0], skip_special_tokens=True)

    # Display the model's reply
    chat_log.insert(tk.END, "You: " + user_input + "\n", "bot")
    chat_log.insert(tk.END, "Neo-GPT: " + response + "\n\n", "bot")

    input_text.delete("1.0", tk.END)

# Run the GUI main loop
window.mainloop()
