import subprocess
import webbrowser

print("DAN-GPT Install Wizard")
packages = ['openai', 'time', 'tensorflow', 'tkinter']

for package in packages:
    try:
        subprocess.check_call(['pip', 'install', package])
        print(f"Successfully installed {package}")
    except subprocess.CalledProcessError:
        print(f"Error installing {package}")

print("Download Sites")
webbrowser.open('https://drive.google.com/drive/folders/1IcthGbPMal1NEkYxQup1wjBWn05Nxomu?usp=sharing')
webbrowser.open('https://sites.google.com/view/dangpt/home')
webbrowser.open('htt[s://www.dan-gpt.space]')
webbrowser.open('https://github.com/WilloDude/dangpt')