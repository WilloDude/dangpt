import tkinter as tk
import requests

class ChatGPT:
    def __init__(self):
        self.api_key = "YOUR_API_KEY_HERE"
        self.api_url = "https://api.openai.com/v1/engines/davinci-codex/completions"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        
        self.window = tk.Tk()
        self.window.title("ChatGPT")
        
        self.message_display = tk.Text(self.window)
        self.message_display.pack()
        
        self.input_entry = tk.Entry(self.window)
        self.input_entry.pack()
        self.input_entry.bind("<Return>", self.send_message)
        
        self.send_button = tk.Button(self.window, text="Send", command=self.send_message)
        self.send_button.pack()
        
        self.window.mainloop()
    
    def send_message(self, event=None):
        message = self.input_entry.get()
        self.input_entry.delete(0, tk.END)
        
        if message:
            response = self.send_api_request(message)
            self.message_display.insert(tk.END, f"You: {message}\nChatGPT: {response}\n\n")
    
    def send_api_request(self, message):
        data = {
            "prompt": f"chat with the model\nUser: {message}\nAI:",
            "max_tokens": 50,
            "temperature": 0.7
        }
        
        response = requests.post(self.api_url, json=data, headers=self.headers)
        
        if response.status_code == 200:
            return response.json()["choices"][0]["text"]
        else:
            return f"An error occurred: {response.json()['error']['message']}"

if __name__ == "__main__":
    ChatGPT()
